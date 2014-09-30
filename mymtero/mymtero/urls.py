from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

#uncomment the next 2 lines to enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'metro.views.home', name='home'),
                       
                       url(r'^about/', 'metro.views.about', name='about'),
                       
                       url(r'^info/', 'metro.views.info', name='info'),
                       
                       url(r'^directions/', 'metro.views.directions', name='directions'),
                       
                       url(r'^nearest/', 'metro.views.nearest', name='nearest'),
                       
                       url(r'^home/', 'metro.views.home', name='home'),
                       
                       
                       
                       #uncomment the next 2 lines to enable admin
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()






