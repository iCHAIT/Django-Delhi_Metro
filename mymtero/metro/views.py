from django.shortcuts import render,render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db import connection

from .forms import distForm


# Create your views here.

def home(request):
    return render_to_response('index.html')

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

def info(request):
    return render_to_response('info.html')

def review(request):
    return render_to_response('review.html')


def directions(request):
    
    form = distForm(request.POST or None)
    if form.is_valid():
        start = form.cleaned_data['start']
        end = form.cleaned_data['end']
        cursor = connection.cursor()
        cursor.execute("call find_path(%s,%s)",[start,end])
        abcd = cursor.fetchall()
        for i in abcd:
            print i[0]
    context = {"form": form}
    template = "directions.html"
    return render(request, template, context)

def nearest(request):
    return render_to_response('nearest.html')


