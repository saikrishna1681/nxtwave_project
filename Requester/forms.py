from django import forms

class Transport_form(forms.Form):
    From=forms.CharField(max_length=200)
    To=forms.CharField(max_length=200)
    date_and_time=forms.DateTimeField()
    flexible_timings=forms.BooleanField(required=False)
    no_of_assets=forms.IntegerField(min_value=1)
    asset_type = forms.ChoiceField(
        choices=(("LAPTOP", "LAPTOP"), ("TRAVEL_BAG", "TRAVEL_BAG"), ("PACKAGE", "PACKAGE"))
    )
    asset_sensitivity = forms.ChoiceField(
        choices=(("HIGHLY_SENSITIVE","HIGHLY_SENSITIVE"),("SENSITIVE","SENSITIVE"),("NORMAL","NORMAL"))
    )
    whom_to_deliver=forms.CharField(max_length=200)

class Travel_info_form(forms.Form):
    From=forms.CharField(max_length=200)
    To=forms.CharField(max_length=200)
    date_and_time=forms.DateTimeField()
    flexible_timings=forms.BooleanField(required=False)
    assets_quantity=forms.IntegerField(min_value=1)
    travel_medium = forms.ChoiceField(
        choices=(("CAR", "CAR"), ("TRAIN", "TRAIN"), ("BUS", "BUS"))
    )