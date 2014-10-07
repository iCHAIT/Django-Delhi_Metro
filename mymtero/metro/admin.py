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
    search_fields = ('sname',)
    exclude = ('sid',)
    list_filter = ('sname',)


class placesAdmin(admin.ModelAdmin):
    list_display = ('sname', 'place')
    search_fields = ('sname',)
    exclude = ('sid',)
    list_filter = ('sname',)

class pathAdmin(admin.ModelAdmin):
    list_display = ('pathid', 'fromsid', 'tosid')
    search_fields = ('pathid',)
    list_filter = ('pathid',)

class reviewAdmin(admin.ModelAdmin):
    list_display = ('sname', 'author', 'timest')
    search_fields = ('sname',)
    list_filter = ('sname',)




# Register your models here.

admin.site.register(stationinfo, stationinfoAdmin)

admin.site.register(station, stationAdmin)

admin.site.register(places, placesAdmin)

admin.site.register(path, pathAdmin)

admin.site.register(review, reviewAdmin)

