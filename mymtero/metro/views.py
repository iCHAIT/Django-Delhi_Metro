from django.shortcuts import render_to_response, RequestContext

#from .forms import EmailForm

#from .models import Join

# Create your views here.

def home(request):
    
    return render_to_response('index.html')

def about(request):
    #print request.POST["email"]
    
    #This is using regular django forms
    '''
    form = EmailForm(request.POST or None)#validation
        if form.is_valid():
            email = form.cleaned_data['email']
                new_join, created = Join.objects.get_or_create(email=email)
                print new_join, created
                print new_join.timestamp
                if created:
                    print "This obj was created"
    
    
    
        #This is using models form
        
        #form = JoinForm(request.POST or None)
        
        
        context = {"form": form}
    return render_to_response('about.html', context, context_instance=RequestContext(request))
'''
    return render_to_response('about.html')

def info(request):
    return render_to_response('info.html')


def directions(request):
    return render_to_response('directions.html')

def nearest(request):
    return render_to_response('nearest.html')


