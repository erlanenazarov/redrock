from django import forms


class TripForm(forms.Form):
    fromdate = forms.CharField(max_length=1000, required=False)
    todate = forms.CharField(max_length=1000, required=False)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=False)
    country = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    people = forms.IntegerField(required=False)
    countchildren = forms.IntegerField(required=False)

