from django.shortcuts import render,render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db import connection

from .forms import dirForm

from .forms import infoForm

from .forms import nearForm

from .forms import revForm


# Create your views here.

def home(request):
    return render_to_response('index.html')


def directions(request):
    form = dirForm(request.POST or None)
    if form.is_valid():
        source = form.cleaned_data['source']
        dest = form.cleaned_data['dest']
        cursor = connection.cursor()
        cursor.execute("call find_path(%s,%s)",[source,dist])
        data = cursor.fetchall()
        for i in data:
            print i[0]
    context = {"form": form}
    template = "directions.html"
    return render(request, template, context)


def directions2(request):
        form = dirForm(request. POST or None)
        if form.is_valid():
            source = request.form['source']
            dest = request.form['dest']
            cursor = connection.cursor()
            cursor.execute("CALL find_path('"+ source +"','"+ dest +"')")
            data = cursor.fetchall()
            for i in data:
                print i[0]
            context = {"form": form}
            template = "directions2.html"
            return render_template(request, template, context)
        else:
            return render_to_response('directions2.html')


def info(request):
    form = infoForm(request.POST or None)
    if form.is_valid():
        statname = form.cleaned_data['statname']
        cursor = connection.cursor()
        cursor.execute("SELECT distinct sname from metro_stationinfo")
        data = cursor.fetchall()
        for i in data:
            print i
    context = {"form": form}
    template = "info.html"
    return render(request, template, context)


def info2(request):
    form = infoForm(request.POST or None)
    if form.is_valid():
        statname = form.cleaned_data['statname']
        cursor = connection.cursor()
        cursor.execute("SELECT * from metro_facility where sname = '" + name + "'")
        infor = cursor.fetchone()
        cursor.execute("SELECT * from metro_stations where sname = '" + name + "'")
        inform = cursor.fetchall()
        cursor.execute("SELECT pname from metro_places where sname = '" + name + "'")
        informa = cursor.fetchall()
        for i in infor:
            print i
        for i in inform:
            print i
        for i in informa:
            print i
        context = {"form": form}
        template = "info2.html"
        return render(request, template, context)
    else:
            return render_to_response('info2.html')


def nearest(request):
    form = nearForm(request.POST or None)
    if form.is_valid():
        if info == 'pin':
            pincode = form.cleaned_data['pincode']
            cursor = connection.cursor()
            cursor.execute("SELECT sname from metro_facility where pincode = '"+ pincode +"'")
            data = cursor.fetchall()
        if info == 'near':
            place = form.cleaned_data['place']
            cursor = connection.cursor()
            cursor.execute("SELECT sname from metro_places where pname = '" + place +"'")
            data = cursor.fetchall()
        for i in data:
            print i
    context = {"form": form}
    template = "nearest.html"
    return render(request, template, context)


def nearest2(request):
    return render_to_response('nearest2.html')


def review(request):
    form = revForm(request.POST or None)
    if form.is_valid():
        statname = form.cleaned_data['statname']
        cursor = connection().cursor()
        cursor.execute("SELECT distinct sname from metro_stationinfo")
        data = cursor.fetchall()
        for i in data:
            print i
    context = {"form": form}
    template = "review.html"
    return render(request, template, context)


def review2(request):
    form = revForm(request.POST or None)
    if form.is_valid():
        statname = form.cleaned_data['statname']
        cursor = connection.cursor()
        cursor.execute("SELECT title,author,timest,bodytext from reviews where sname = '"+ name +"'")
        data = cursor.fetchall()
        for i in data:
            print i
    context = {"form": form}
    template = "review2.html"
    return render_to_response('review2.html')


def about(request):
    '''
    form = EmailForm(request.POST or None)
    if form.is_valid():
        email =  form.cleaned_data['email']
        new_join, created = Join.objects.get_or_create(email=email)
        print new_join, created
        
    form = abcForm(request.POST or None)
    if form.is_valid():
        new_abc = form.save(commit=False)
        new_abc.save()

    context = {"form": form}
    template = "about.html"
    '''
    return render_to_response('about.html')





