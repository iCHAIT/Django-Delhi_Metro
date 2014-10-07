from django import forms

from .models import dir


class dirForm(forms.Form):
    source = forms.CharField()
    dest = forms.CharField()

class infoForm(forms.Form):
    statname = forms.CharField()

class reviewForm(forms.Form):
    statname = forms.CharField()

class nearForm(forms.Form):
    place = forms.CharField(required = False)
    pincode = forms.IntegerField(required = False)