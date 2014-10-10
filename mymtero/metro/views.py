from django.shortcuts import render,render_to_response, RequestContext

from django.http import HttpResponse, request

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
'''
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
'''
def directions(request):
    form = dirForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("select sname from metro_stationinfo")
    data = cursor.fetchall()
    return render_to_response('directions.html', {'data': data})


def directions2(request):
    form = dirForm(request.POST or None)
    if form.is_valid():
        source = form['source']
        dest = form.cleaned_data['dest']
        cursor = connection.cursor()
        cursor.execute("call find_path(%s,%s)",[source,dest])
        data = cursor.fetchall()
    return render_to_response( 'directions2.html', {'data': data, 'source': source, 'dest': dest})



def info(request):
    form = infoForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("select sname from metro_stationinfo")
    data = cursor.fetchall()
    return render_to_response('info.html', {'data': data},context_instance = RequestContext(request))


'''
    def user_profile(request):
    if request.method == 'POST':
    form = UserProfileForm(request.POST, instance=request.user.profile)
    if form.is_valid():
    form.save()
    return HttpResponseRedirect('/accounts/loggedin')
    '''

def info2(request):
    form = infoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            sname = form.get['sname']
            form.save()
            return HttpResponse('info2.html')

    '''
    form = infoForm(request.POST or None)
    if form.is_valid():
        sname = 'Khan Market'
        print sname
        cursor = connection.cursor()
        cursor.execute("SELECT * from metro_stationinfo where sname = %s",[sname])
        infor = cursor.fetchone()
        cursor.execute("SELECT * from metro_station where sname =%s",[sname])
        inform = cursor.fetchall()
        cursor.execute("SELECT place from metro_places where sname =%s",[sname])
        informa = cursor.fetchall()
        return render_to_response('info2.html',{'infor': infor,'inform': inform,'informa': informa})
        '''



def nearest(request):
    form1 = near1Form(request.POST or None)
    form2 = near2Form(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("select place from metro_places")
    data = cursor.fetchall()
    cursor.execute("select pincode from metro_stationinfo")
    data1 = cursor.fetchall()
    return render_to_response('nearest.html', {'data': data,'data1':data1})

def nearest2(request):
    form1 = near1Form(request.POST or None)
    cursor = connection.cursor()
    if form1.is_valid():
        place = form1.cleaned_data['place']
        cursor.execute("SELECT sname from metro_places where place =%s",[place])
        data = cursor.fetchall()
        return render_to_response('nearest2.html', {'data':data})

def nearest3(request):
    form2 = near2Form(request.POST or None)
    if form2.is_valid():
        pin = form2.cleaned_data['pin']
        cursor = connection.cursor()
        cursor.execute("SELECT sname from metro_stationinfo where pincode =%s",[pin])
        data = cursor.fetchall()
    return render_to_response('nearest2.html', {'data': data})


def review(request):
    form1 = rev1Form(request.POST or None)
    form2 = rev2Form(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("select sname from metro_stationinfo")
    data = cursor.fetchall()
    return render_to_response('review.html', {'data': data})


def review2(request):
    form1 = rev1Form(request.POST or None)
    if form1.is_valid():
        sname = form1.cleaned_data['sname']
        cursor = connection.cursor()
        cursor.execute("SELECT sname,title,author,bodytext from metro_review where approved = 'no'")
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
    return render_to_response('review2.html')


def about(request):
    return render_to_response('about.html')





