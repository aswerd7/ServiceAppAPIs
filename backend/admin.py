from django.contrib import admin
from .models import Worker, Schedule, Location, Appointment
from django.contrib.auth.models import Group

# Насройки админ панели ----------


admin.site.site_header = "Управление записями"

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('idSpec', 'date',)
    list_filter = ('date', 'idSpec',)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Spec')
    list_filter = ('Spec', )
    
@admin.register(Location)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('LocName','id',)

@admin.register(Appointment)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('Cname', 'Cphone', 'Spec', 'date',)
    list_filter = ('Spec', 'Cname')
    
    
admin.site.unregister(Group)