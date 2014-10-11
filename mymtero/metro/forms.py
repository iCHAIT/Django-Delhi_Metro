from django import forms


from .models import dir

from .models import info

from .models import near1

from .models import near2

from .models import rev1

from .models import rev2



'''
class dirForm(forms.Form):
    source = forms.ChoiceField(widget=forms.Select)
    dest = forms.CharField()


class infoForm(forms.Form):
    sname = forms.CharField()


class near1Form(forms.Form):
    place = forms.CharField()


class near2Form(forms.Form):
    pin = forms.IntegerField()


class rev1Form(forms.Form):
    sname = forms.CharField()

class rev2Form(forms.Form):
    sname = forms.CharField()
    title = forms.CharField()
    bodytext = forms.CharField()
    author = forms.CharField()

'''

class dirForm(forms.Form):
    CHOICES = (
    
            ('Rajiv Chowk', 'Rajiv Chowk'),
            ('Patel Chowk', 'Patel Chowk'),
    
        )
    source = forms.ChoiceField(choices = CHOICES)
    dest = forms.ChoiceField(choices = CHOICES)


class infoForm(forms.Form):
    CHOICES = (
               
               ('Rajiv Chowk', 'Rajiv Chowk'),
               ('Patel Chowk', 'Patel Chowk'),
               
               )
    sname = forms.ChoiceField(choices = CHOICES)


class near1Form(forms.Form):
    place = forms.CharField()


class near2Form(forms.Form):
    CHOICES = (
    
        ('110003', '110003'),
        ('110034', '110034')
    
        )
    pin = forms.ChoiceField(choices = CHOICES)


class rev1Form(forms.Form):
    CHOICES = (
               
               ('Rajiv Chowk', 'Rajiv Chowk'),
               ('Patel Chowk', 'Patel Chowk'),
               
               )
    sname = forms.ChoiceField(choices = CHOICES)

class rev2Form(forms.Form):
    CHOICES = (
               
               ('Rajiv Chowk', 'Rajiv Chowk'),
               ('Patel Chowk', 'Patel Chowk'),
               
               )
    sname = forms.ChoiceField(choices = CHOICES)
    title = forms.CharField()
    bodytext = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()


