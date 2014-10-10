from django.conf.urls import patterns, include, url

from django.conf import settings

from django.conf.urls.static import static

#uncomment the next 2 lines to enable admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'metro.views.home', name='home'),
                       
                       url(r'^home/', 'metro.views.home', name='home'),
                       
                       url(r'^directions/', 'metro.views.directions', name='directions'),
                       
                       url(r'^directions2/', 'metro.views.directions2', name='directions2'),
                       
                       url(r'^info/', 'metro.views.info', name='info'),
                       
                       url(r'^info2/', 'metro.views.info2', name='info2'),
                       
                       url(r'^nearest/', 'metro.views.nearest', name='nearest'),
                       
                       url(r'^nearest2/', 'metro.views.nearest2', name='nearest2'),

                       url(r'^nearest3/', 'metro.views.nearest3', name='nearest3'),
                       
                       url(r'^review/','metro.views.review', name='review'),
                       
                       url(r'^review2/','metro.views.review2', name='review2'),

                       
                       url(r'^review3/','metro.views.review3', name='review3'),
                       
                       
                       url(r'^about/', 'metro.views.about', name='about'),
                       
                       
                       #uncomment the next 2 lines to enable admin
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()






