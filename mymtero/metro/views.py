from django.shortcuts import render_to_response, RequestContext

from metro.models import station

from metro.models import facility

from metro.models import places

from metro.models import junction

from metro.models import blog

from metro.models import lostfound

from metro.models import admin

# Create your views here.

def home(request):
    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')


def info(request):
    return render_to_response('info.html')


def directions(request):
    return render_to_response('directions.html')

def nearest(request):
    return render_to_response('nearest.html')

def blog(request):
    entries = blog.objects.all()[:5]
    return render_to_response('blog.html', {'blog' : entries})

