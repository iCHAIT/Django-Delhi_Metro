from django import forms

from .models import dist


class distForm(forms.Form):
    start = forms.CharField()
    end = forms.CharField()

class infoForm(forms.Form):
    statname = forms.CharField()

class reviewForm(forms.Form):
    statname = forms.CharField()

class nearForm(forms.Form):
    place = forms.CharField(required = False)
    pincode = forms.BigIntegerField(required = False)