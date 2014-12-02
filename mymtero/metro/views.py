from django.shortcuts import render_to_response, RequestContext

from django.db import connection

from django import forms

from .models import dir
from .forms import dirForm

from .models import info
from .forms import infoForm

from .models import near1
from .forms import near1Form

from .models import near2
from .forms import near2Form

from .models import rev1
from .forms import rev1Form

from .models import rev2
from .forms import rev2Form


# Create your views here.


def home(request):
    return render_to_response('index.html')


def directions(request):
    form = dirForm(request.POST or None)
    return render_to_response('directions.html', {'form': form}, context_instance = RequestContext(request))


def directions2(request):
    form = dirForm(request.POST or None)
    if form.is_valid():
        source = form.cleaned_data['source']
        dest = form.cleaned_data['dest']
        cursor = connection.cursor()
        cursor.execute("call find_path(%s,%s)",[source,dest])
        data = cursor.fetchall()
    return render_to_response( 'directions2.html', {'data': data, 'source': source, 'dest': dest})



def info(request):
    form = infoForm(request.POST or None)
    return render_to_response('info.html', {'form': form}, context_instance = RequestContext(request))



def info2(request):
    form = infoForm(request.POST or None)
    if form.is_valid():
        sname = form.cleaned_data['sname']
        cursor = connection.cursor()
        cursor.execute("SELECT * from metro_stationinfo where sname = %s",[sname])
        infor = cursor.fetchone()
        cursor.execute("SELECT * from metro_station where sname =%s",[sname])
        inform = cursor.fetchall()
        cursor.execute("SELECT place from metro_places where sname =%s",[sname])
        informa = cursor.fetchall()
        return render_to_response('info2.html',{'infor': infor,'inform': inform,'informa': informa})



def nearest(request):
    form1 = near1Form(request.POST or None)
    form2 = near2Form(request.POST or None)
    return render_to_response('nearest.html', {'form1': form1,'form2':form2}, context_instance = RequestContext(request))


def nearest2(request):
    form1 = near1Form(request.POST or None)
    cursor = connection.cursor()
    if form1.is_valid():
        place = form1.cleaned_data['place']
        cursor.execute("SELECT sname from metro_places where place =%s",[place])
        data1 = cursor.fetchall()
        return render_to_response('nearest2.html', {'data1':data1})

def nearest3(request):
    form2 = near2Form(request.POST or None)
    if form2.is_valid():
        pin = form2.cleaned_data['pin']
        cursor = connection.cursor()
        cursor.execute("SELECT sname from metro_stationinfo where pincode =%s",[pin])
        data2 = cursor.fetchall()
    return render_to_response('nearest2.html', {'data2': data2})


def review(request):
    form1 = rev1Form(request.POST or None)
    form2 = rev2Form(request.POST or None)
    return render_to_response('review.html', {'form1': form1, 'form2': form2}, context_instance = RequestContext(request))


def review2(request):
    form1 = rev1Form(request.POST or None)
    if form1.is_valid():
        sname = form1.cleaned_data['sname']
        cursor = connection.cursor()
        cursor.execute("SELECT sname,title,author,bodytext from metro_review where approved = 'Yes'")
        data = cursor.fetchall()
    return render_to_response('review2.html', {'data': data})

def review3(request):
    form2 = rev2Form(request.POST or None)
    if form2.is_valid():
        sname = form2.cleaned_data['sname']
        title = form2.cleaned_data['title']
        bodytext = form2.cleaned_data['bodytext']
        author = form2.cleaned_data['author']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO metro_review (sname,title,author,bodytext,timest,approved) VALUES (%s,%s,%s,%s,now(),'no')",[sname,title,author,bodytext])
        cursor.execute('COMMIT')
    data = "Review has been added. It will be displayed once approved by the admin."
    return render_to_response('boilerplate.html', {'data': data})


def about(request):
    return render_to_response('about.html')



