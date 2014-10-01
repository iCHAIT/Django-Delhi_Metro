from django.contrib import admin


from metro.models import station
from metro.models import stationinfo
from metro.models import places
from metro.models import review
from metro.models import validpath
#from metro.models import Join



class stationinfoAdmin(admin.ModelAdmin):
    list_display = ('sname','washroom','parking','elevator','contact','opening_date','pincode')
    search_fields = ['sname']


class stationAdmin(admin.ModelAdmin):
    list_display = ('statname', 'line', 'grade',)
    search_fields = ['statname']


class placesAdmin(admin.ModelAdmin):
    list_display = ('statname', 'place',)
    search_fields = ['statsname']





# Register your models here.
admin.site.register(stationinfo, stationinfoAdmin)

admin.site.register(station, stationAdmin)

admin.site.register(places, placesAdmin)

#admin.site.register(review)

#admin.site.register()