from django.shortcuts import render_to_response, RequestContext
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
    return render_to_response('blog.html')

