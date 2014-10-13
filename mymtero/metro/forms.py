from django import forms

from django.db import connection

from .models import dir

from .models import info

from .models import near1

from .models import near2

from .models import rev1

from .models import rev2




class dirForm(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select sname,sname from metro_stationinfo")
    CHOICES = cursor.fetchall()
    source = forms.ChoiceField(choices = CHOICES)
    dest = forms.ChoiceField(choices = CHOICES)


class infoForm(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select sname,sname from metro_stationinfo")
    CHOICES = cursor.fetchall()
    sname = forms.ChoiceField(choices = CHOICES)


class near1Form(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select place,place from metro_places")
    CHOICES = cursor.fetchall()
    place = forms.ChoiceField(choices = CHOICES)


class near2Form(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select pincode,pincode from metro_stationinfo")
    CHOICES = cursor.fetchall()
    pin = forms.ChoiceField(choices = CHOICES)


class rev1Form(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select sname,sname from metro_stationinfo")
    CHOICES = cursor.fetchall()
    sname = forms.ChoiceField(choices = CHOICES)

class rev2Form(forms.Form):
    cursor = connection.cursor()
    cursor.execute("select sname,sname from metro_stationinfo")
    CHOICES = cursor.fetchall()
    sname = forms.ChoiceField(choices = CHOICES)
    title = forms.CharField()
    bodytext = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()


