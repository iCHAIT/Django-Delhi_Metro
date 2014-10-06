from django import forms

from .models import dist


class distForm(forms.Form):
    start = forms.CharField()
    end = forms.CharField()

