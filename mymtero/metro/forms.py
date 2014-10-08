from django import forms

from .models import dir

from .models import info

from .models import near1

from .models import near2

from .models import rev1

from .models import rev2


class dirForm(forms.Form):
    source = forms.CharField()
    dest = forms.CharField()


class infoForm(forms.Form):
    sname = forms.CharField()


class near1Form(forms.Form):
    place = forms.CharField(required = False)

class near2Form(forms.Form):
    pin = forms.IntegerField(required = False)


class rev1Form(forms.Form):
    sname = forms.CharField()

class rev2Form(forms.Form):
    sname = forms.CharField()
    title = forms.CharField()
    bodytext = forms.CharField()
    author = forms.CharField()