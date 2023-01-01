#from views import *
from django.urls import path
from  . import views


urlpatterns=[

    path("logout",views.logout_user,name="logout"),
    path("login_page",views.login_page,name="login_page"),
    path("login",views.login_function,name="login_function"),
    path("home", views.home,name="home"),
    path("", views.home,name="home"),
    
    
    path("transport_form", views.transport_form,name="transport_form"),
    path("rider_form", views.rider_form,name="rider_form"),
    path("my_transportation_requests",views.my_transportation_requests,name="transportation_request"),
    path("view_matched_rides/<int:transport_request_id>",views.get_matchingrides,name="get_matchingrides"),

    path("submit_transport_request", views.submit_transport_request,name="submit_transport_request"),
    path("submit_travel_info", views.submit_travel_info,name="submit_travel_info"),
    path("change_applystatus/<int:transport_request_id>/<int:ride_id>", views.change_applystatus,name="change_applystatus")
]