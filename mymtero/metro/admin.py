from django.contrib import admin

from metro.models import stationinfo

from metro.models import station

from metro.models import places

from metro.models import path

from metro.models import review


class stationinfoAdmin(admin.ModelAdmin):
    list_display = ('sname','washroom','parking','elevator','opening_date','contact','pincode')
    search_fields = ('sname',)
    exclude = ('cost','pathid','calculated')
    list_filter = ('sname', 'pincode')



class stationAdmin(admin.ModelAdmin):
    list_display = ('sname', 'line', 'grade')
    search_fields = ['sname']


class placesAdmin(admin.ModelAdmin):
    list_display = ('sname', 'place')
    search_fields = ['sname']





# Register your models here.
admin.site.register(stationinfo)

admin.site.register(station, stationAdmin)

admin.site.register(places, placesAdmin)

admin.site.register(path)

admin.site.register(review)

#admin.site.register(review)

#admin.site.register()