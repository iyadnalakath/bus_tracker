from django.contrib import admin
from .models import *
# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'bus_stop_name',
        'location'

    )


admin.site.register(BusStop,BusStopAdmin)


class BusAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'bus_name',
        'route'
    )

admin.site.register(Bus,BusAdmin)


class BusTimeAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'bus_stop',
        'bus',
        'time'
    )

admin.site.register(BusTime,BusTimeAdmin)