from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

        
class Worker(models.Model):
    Name = models.CharField(verbose_name='Имя', max_length=64)
    Spec = models.CharField(verbose_name='Специальность', max_length=64)
    
    def __str__(self):
        return str(self.Name)
    
class Location(models.Model):
    LocName = models.CharField(verbose_name='Место Работы', max_length=64)
    
    def __str__(self):
        return str(self.LocName)
    
class Schedule(models.Model):
    idSpec = models.ForeignKey(Worker, verbose_name='Специалист', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата')
    start = models.TimeField(verbose_name='Начало Работы')
    end = models.TimeField(verbose_name='Конец Работы')
    
    def __str__(self):
        return (str(self.idSpec))
    
class Appointment(models.Model):
    Cname = models.CharField(verbose_name='Имя', max_length=32)
    Cphone = PhoneNumberField(verbose_name='Номер')
    Spec = models.ForeignKey(Worker, verbose_name='Специалист', on_delete=models.DO_NOTHING)
    Order = models.CharField(verbose_name='Цель', max_length=64)
    date = models.DateField(verbose_name='Дата')
    start = models.TimeField(verbose_name='Начало Работы')
    end = models.TimeField(verbose_name='Конец Работы')
    Loc = models.ForeignKey(Location, verbose_name='Место', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.Cname)
    