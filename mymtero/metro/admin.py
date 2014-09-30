from django.contrib import admin


from metro.models import station
from metro.models import stationinfo
from metro.models import places
from metro.models import junction
from metro.models import review
from metro.models import Join



class stationinfoAdmin(admin.ModelAdmin):
    list_display = ('sname', 'contact',)
    search_fields = ['sname']


class stationAdmin(admin.ModelAdmin):
    list_display = ('statname', 'line', 'pincode', 'grade',)
    search_fields = ['statname']


class placesAdmin(admin.ModelAdmin):
    list_display = ('statname', 'place',)
    search_fields = ['statsname']


class junctionAdmin(admin.ModelAdmin):
    list_display = ('statname', 'line1', 'line2',)
    search_fields = ['statname']




# Register your models here.

admin.site.register(station, stationAdmin)

admin.site.register(stationinfo, stationinfoAdmin)

admin.site.register(places, placesAdmin)

admin.site.register(junction, junctionAdmin)

admin.site.register(review)

admin.site.register(Join)