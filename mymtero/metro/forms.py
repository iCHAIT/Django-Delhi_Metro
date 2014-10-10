from django import forms

from .models import dir

from .models import info

from .models import near1

from .models import near2

from .models import rev1

from .models import rev2

from django.forms.widgets import Select

from django.forms import widgets


class dirForm(forms.Form):
    SOURCE_CHOICES = (
               ('KM', 'Khan Market'),
               ('KG', 'Kashmere Gates'),
               )
    source = forms.CharField(widget=forms.Select)
#    dest = forms.CharField()
    dest = forms.ChoiceField(choices = SOURCE_CHOICES, widget=forms.Select())


class infoForm(forms.Form):
    sname = forms.CharField()


class near1Form(forms.Form):
    place = forms.CharField(required = False)

class near2Form(forms.Form):
    pin = forms.IntegerField(required = False)


class rev1Form(forms.Form):
    sname = forms.CharField(required = False)

class rev2Form(forms.Form):
    sname = forms.CharField(required = False)
    title = forms.CharField(required = False)
    #    bodytext = forms.CharField(widget=forms.Textarea)
    bodytext = forms.CharField(widget = forms.Textarea(),)
    author = forms.CharField(required = False)



'''
                             title = forms.CharField(max_length=3,
                                                     widget=forms.Select(choices=TITLE_CHOICES))
                                                     
                                                     sex = ChoiceField(label='', choices=SEX, widget=forms.Select(attrs={'class':'regDropDown'}))



                             TITLE_CHOICES = (
                                              ('MR', 'Mr.'),
                                              ('MRS', 'Mrs.'),
                                              ('MS', 'Ms.'),
                                              )'''