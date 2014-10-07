from django import forms

from .models import dir

from .models import info

from .models import near

from .models import rev

class dirForm(forms.Form):
    source = forms.CharField()
    dest = forms.CharField()


class infoForm(forms.Form):
    statname = forms.CharField()


class nearForm(forms.Form):
    place = forms.CharField(required = False)
    pin = forms.IntegerField(required = False)


class revForm(forms.Form):
    statname = forms.CharField()
