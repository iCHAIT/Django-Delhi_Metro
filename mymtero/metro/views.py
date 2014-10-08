from django.shortcuts import render,render_to_response, RequestContext

from django.core.context_processors import csrf

from django.db import connection


from django import forms

from metro.forms import dirForm

from metro.forms import infoForm

from metro.forms import near1Form

from metro.forms import near2Form

from metro.forms import rev1Form

from metro.forms import rev2Form


# Create your views here.

def home(request):
    return render_to_response('index.html')


def directions(request):
    form = dirForm(request.POST or None)
    context = {"form": form}
    template = "directions.html"
    return render(request, template, context)


def directions2(request):
    form = dirForm(request.POST or None)
    if form.is_valid():
        source = form.cleaned_data['source']
        dest = form.cleaned_data['dest']
        cursor = connection.cursor()
        cursor.execute("call find_path(%s,%s)",[source,dest])
        data = cursor.fetchall()
    return render_to_response('directions2.html',{'data':data,'source':source,'dest':dest})



def info(request):
    form = infoForm(request.POST or None)
    context = {"form": form}
    template = "info.html"
    return render(request, template, context)


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
        return render_to_response('info2.html',{"infor":infor, "inform":inform, "informa":informa})


def nearest(request):
    form1 = near1Form(request.POST or None)
    form2 = near2Form(request.POST or None)
    context = {"form1": form1,"form2": form2}
    template = "nearest.html"
    return render(request, template, context)

def nearest2(request):
    form1 = near1Form(request.POST or None)
    if form1.is_valid():
        place = form1.cleaned_data['place']
        cursor = connection.cursor()
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
    context = {"form1": form1,"form2": form2}
    template = "review.html"
    return render(request, template, context)


def review2(request):
    form1 = rev1Form(request.POST or None)
    form2 = rev2Form(request.POST or None)
    if form1.is_valid():
        sname = form1.cleaned_data['sname']
        cursor = connection.cursor()
        cursor.execute("SELECT sname,title,author,bodytext from metro_review where approved = 'Yes'")
        data = cursor.fetchall()
    if form2.is_valid():
        sname = form2.cleaned_data['sname']
        title = form2.cleaned_data['title']
        bodytext = form2.cleaned_data['bodytext']
        author = form2.cleaned_data['author']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO metro_review  ('sname') VALUES %s",[sname])
        data = cursor.fetchall()
    return render_to_response('review2.html', {'data': data})


def about(request):
    return render_to_response('about.html')





