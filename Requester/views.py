from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

from django.contrib.auth import authenticate, login

def login_function(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request,"success")
        return render(request,"Home.html")
    else:
        # Return an 'invalid login' error message.
        messages.error(request,"invalid credentials")
        return render(request,"Home.html")

def logout_user(request):
    logout(request)
    return render(request,"base.html")

def home(request):
    return render(request,"Home.html")

def login_page(request):
    return render(request,"Login.html")


def transport_form(request):
    return render(request,"Transport_form.html", {"transport_form":Transport_form})
    

def rider_form(request):
    return render(request,"Rider_form.html", {"rider_form":Travel_info_form})


def my_transportation_requests(request):
    #requester=1
    requester=request.user.id
    my_requests=Transport_Request.objects.filter(requester=requester)
    required_data=[]
    for i in my_requests:
        temp={"id":i.id,"FROM":i.pickup,"TO":i.delivery_at, 'date_time':i.date_time,
            "asset_type":i.asset_types,"asset_sensitivity":i.sensitivities,
            "whom_to_deliver":i.whom_to_deliver,"accepted_person_details":i.rider,
            "status":i.status, "assets_quantity":i.assets_quantity
            }
        required_data.append(temp)
    return render(request,"Transportation_requests.html",{"required_data":required_data})


def get_matchingrides(request,transport_request_id):
    #transport_request_id=1
    transport_request_object=Transport_Request.objects.get(id=transport_request_id)
    date_time=transport_request_object.date_time
    pickup=transport_request_object.pickup
    pickup=pickup.split()[-1].lower()
    delivery_at=transport_request_object.delivery_at
    delivery_at=delivery_at.split()[-1].lower()
    print(pickup,delivery_at)
    matched_rides=Travel_info.objects.filter(date_time=date_time,
        pickup=pickup,delivery_at=delivery_at)
    required_data=[]
    for i in matched_rides:
        # applied_rides=Applied_Rides.objects.filter(requester_id=request.user.id,rider_id=i.id,
        #     transport_request_id=transport_request_id)
        status="NOT APPLIED"
        id=i.id
        #print(applied_rides)
        if i in transport_request_object.travel_info_set.all():
            status="APPLIED"
        temp={"FROM":i.pickup,"TO":i.delivery_at, 'date_time':i.date_time,
            "status":status, "luggage_quantity":i.assets_quantity, 
            'id':id
            }
        required_data.append(temp)
    print(required_data)
    
    return render(request,"Matched_rides.html",{"required_data":required_data,
        "transport_request_id":transport_request_id})


def submit_transport_request(request):
    if request.method == 'POST':
        form = Transport_form(request.POST)
        if form.is_valid():
            From=form.cleaned_data["From"]
            to=form.cleaned_data["To"]
            date_time=form.cleaned_data["date_and_time"]
            flexible_timings=form.cleaned_data["flexible_timings"]
            no_of_assets=form.cleaned_data["no_of_assets"]
            asset_types=form.cleaned_data["asset_type"]
            asset_sensitivity=form.cleaned_data["asset_sensitivity"]
            whom_to_deliver=form.cleaned_data["whom_to_deliver"]
            id=request.user.id
            obj=Transport_Request(requester_id=id,pickup=From,delivery_at=to,
                date_time=date_time,flexible=flexible_timings, 
                whom_to_deliver=whom_to_deliver,asset_types=asset_types,
                assets_quantity=no_of_assets,sensitivities=asset_sensitivity)
            obj.save()
            print(asset_sensitivity,asset_types)
            messages.success(request, "success")
            return HttpResponseRedirect("transport_form")
        else:
            messages.error(request, "error")
            #return render(request,"Transport_form.html")
            return HttpResponseRedirect("transport_form")
            
    else:
        messages.error(request,"wrong method")
        return HttpResponseRedirect("transport_form")

def submit_travel_info(request):
    if request.method == 'POST':
        form = Travel_info_form(request.POST)
        if form.is_valid():
            From=form.cleaned_data["From"]
            to=form.cleaned_data["To"]
            date_time=form.cleaned_data["date_and_time"]
            flexible_timings=form.cleaned_data["flexible_timings"]
            assets_quantity=form.cleaned_data["assets_quantity"]
            travel_medium=form.cleaned_data["travel_medium"]
            id=request.user.id
            From=From.split()[-1].lower()
            to=to.split()[-1].lower()
            obj=Travel_info(rider_id=id,pickup=From,delivery_at=to,
                date_time=date_time,flexible=flexible_timings, 
                assets_quantity=assets_quantity,travel_medium=travel_medium)
            obj.save()
            messages.success(request, "success")
            return HttpResponseRedirect("rider_form")
        else:
            messages.error(request, "invalid form")
            return HttpResponseRedirect("rider_form")
            
    else:
        messages.error(request, "invalid method")
        return HttpResponseRedirect("rider_form")

# def apply_for_ride(request):
#     if request.method == 'POST':
#         form = Travel_info_form(request.POST)
#         if form.is_valid():
#             From=form.cleaned_data["From"]
#             to=form.cleaned_data["To"]
#             date_time=form.cleaned_data["date_and_time"]
#             flexible_timings=form.cleaned_data["flexible_timings"]
#             assets_quantity=form.cleaned_data["assets_quantity"]
#             travel_medium=form.cleaned_data["travel_medium"]
#             obj=Travel_info(rider_id=1,pickup=From,delivery_at=to,
#                 date_time=date_time,flexible=flexible_timings, 
#                 assets_quantity=assets_quantity,travel_medium=travel_medium)
#             obj.save()
#             return HttpResponse("success")    
#         else:
#             print(form.errors)
#             return HttpResponse("invalid form")
            
#     else:
#         return HttpResponse("wrong method used to submit the form")

def change_applystatus(request,transport_request_id,ride_id):
    ride=Travel_info.objects.get(id=ride_id)
    transport=Transport_Request.objects.get(id=transport_request_id)
    if ride in transport.travel_info_set.all():
        transport.travel_info_set.remove(ride)
    else:
        transport.travel_info_set.add(ride)
    messages.success(request, "success")
    return HttpResponseRedirect(f"/view_matched_rides/{transport_request_id}", {"messages":messages})