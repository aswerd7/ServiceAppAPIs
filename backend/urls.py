from django.urls import path, include, re_path
from .views import *


app_name = 'records'
urlpatterns = [
    path('api/v1/workers_list', WorkersList.as_view() ),
    re_path(r'^api/v1/workers_list/f', WorkerFiltered.as_view() ),
    re_path(r'^api/v1/workers_select', WorkerSelectDate.as_view() ),
    re_path(r'^api/v1/appo_check/', AppointmentCheck.as_view() ),
    re_path(r'^api/v1/appo_date/', AppointmentCheckDate.as_view() ),
    path('api/v1/create', appointment),

]
 