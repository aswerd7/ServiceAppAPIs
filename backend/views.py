from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Worker, Schedule, Appointment
from .script import *

# APi для клиентов ------------ Все фильтры через URL параметры /?___=___

# Список спецов
class WorkersList(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
   

# Список спецов с фильтром по профессии
class WorkerFiltered(generics.ListAPIView):
    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        Spec = self.request.query_params.get('Spec')
        return Worker.objects.filter(Spec=Spec)

#Расписание спеца на нужную дату
class WorkerSelectDate(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()
        id = self.request.query_params.get('id')
        date = self.request.query_params.get('date')
        return Schedule.objects.filter(idSpec=id).filter(date=date)
 
 
# APi для спецов ------------

# Список заказов для определенного спеца по его ID 
class AppointmentCheck(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        id = self.request.query_params.get('id')
        return Appointment.objects.filter(Spec=id)

# Также фильтр по дате 
class AppointmentCheckDate(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        id = self.request.query_params.get('id')
        date = self.request.query_params.get('date')
        return Appointment.objects.filter(Spec=id).filter(date=date)
    

# APi для заказа ------------

@api_view(['POST'])
def appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    date = request.data["date"]
    loc = request.data["Loc"]
    start = request.data["start"]
    end = request.data["end"]  
    spec = request.data["Spec"]
# Проверяем заказы в этот день
    checkdata = Appointment.objects.filter(date=date).values()
    for item in checkdata:
# Локации (Согласно ТЗ одна локация один работник)
        if str(item["Loc_id"]) == str(loc):
            startcheck = item["start"]
            endcheck = item["end"]
            if timecheck(start, end, startcheck, endcheck):
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif str(item["Spec_id"]) == str(spec):
# Свободен ли в это время специалист
            startcheck = item["start"]
            endcheck = item["end"]
            if timecheck(start, end, startcheck, endcheck):
                return Response(status=status.HTTP_400_BAD_REQUEST)
# И сверяем с расписанием
    checksched = Schedule.objects.filter(date=date).filter(idSpec=spec).values()
    for i in checksched:
        scstart = i["start"]
        scend = i["end"]
        if timecheckPR(start, end, scstart, scend):
# При успешном проходе всех условий запись заноситься в бд
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
        

