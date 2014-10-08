from django.shortcuts import render,render_to_response, RequestContext

from django.core.context_processors import csrf

from django.db import connection


from .forms import dirForm

from .forms import infoForm

from .forms import near1Form

from .forms import near2Form

from .forms import rev1Form

from .forms import rev2Form


# Create your views here.

def home(request):
    return render_to_response('index.html')


def directions(request):
    form = dirForm(request.POST or None)
    context = {"form": form}
    template = "directions.html"
    return render(request, template, context)


def directions2(request):
    #if form.is_valid():
    source = form.cleaned_data['source']
    dest = form.cleaned_data['dest']
    cursor = connection.cursor()
    cursor.execute("call find_path(%s,%s)",[source,dest])
    data = cursor.fetchall()
    for i in data:
        print i[0]
    return render_to_response('directions2.html',{'data':data})



def info(request):
    form = infoForm(request.POST or None)
    #    context = {"form": form}
    template = "info.html"
    return render(request, template, {"form": form})


def info2(request):
    #if form.is_valid():
    #sname = form.cleaned_data['sname']
    sname = "Khan Market"
    cursor = connection.cursor()
    cursor.execute("SELECT * from metro_stationinfo where sname = %s",[sname])
    infor = cursor.fetchone()
    cursor.execute("SELECT * from metro_station where sname =%s",[sname])
    inform = cursor.fetchall()
    cursor.execute("SELECT pname from metro_places where sname =%s",[sname])
    informa = cursor.fetchall()
    for i in infor:
        print i
    for i in inform:
        print i
    for i in informa:
        print i
    context = {"infor":infor, "inform":inform, "informa":informa}
    template = "info2.html"
    return render(request, template, context)



def nearest(request):
    form1 = near1Form(request.POST or None)
    form2 = near2Form(request.POST or None)
    context = {"form1": form1,"form2": form2}
    template = "nearest.html"
    return render(request, template, context)

def nearest2(request):
    #    if form1.is_valid():
    place = form.cleaned_data['place']
    cursor = connection.cursor()
    cursor.execute("SELECT sname from metro_places where pname =%s",[place])
    data = cursor.fetchall()
        #if form2.is_valid():
        pin = form.cleaned_data['pincode']
        cursor = connection.cursor()
        cursor.execute("SELECT sname from metro_facility where pincode =%s",[pin])
        data = cursor.fetchall()
    for i in data:
        print i
    context = {"form": form}
    template = "nearest2.html"
    return render_to_response('nearest2.html', {'data':data})


def review(request):
    form1 = rev1Form(request.POST or None)
    form2 = rev2Form(request.POST or None)
    context = {"form1": form1,"form2": form2}
    template = "review.html"
    return render(request, template, context)


def review2(request):
    if form1.is_valid():
        sname = form.cleaned_data['sname']
        cursor = connection().cursor()
        cursor.execute("SELECT sname,title,author,bodytext from metro_review where approved = 'Yes'")
        data = cursor.fetchall()
        for i in data:
            print i
    if form2.is_valid():
        sname = form.cleaned_data['sname']
        title = form.cleaned_data['title']
        bodytext = form.cleaned_data['bodytext']
        author = form.cleaned_data['author']
        cursor = connection().cursor()
        cursor.execute("INSERT (sname,title,author,timest,bodytext) into metro_review values %s,%s,%s,%s(now),%s"[sname,title,author,timest,bodytext])
        data = cursor.fetchall()
        for i in data:
            print i
    context = {"data": data}
    template = "review2.html"
    return render(request, template, context)


def about(request):
    return render_to_response('about.html')





