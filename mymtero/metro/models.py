from django.db import models

# Create your models here.

class station(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length = 50)
    line = models.CharField(max_length = 15)
    pincode = models.IntegerField()
    grade = models.CharField(max_length = 15)
    #pk = CompositeField(('sname', 'line'))
#thing.pk.primary_key= True

class facility(models.Model):
    sname = models.CharField(max_length = 50,primary_key = True)
    washroom = models.CharField(max_length = 5)
    elevator = models.CharField(max_length = 5)
    parking = models.CharField(max_length = 5)
    opening_date = models.DateField()
    contact = models.BigIntegerField()
    sname = models.ForeignKey(station)

class places(models.Model):
    sname = models.CharField(max_length = 50,primary_key = True)
    place1 = models.CharField(max_length = 50)
    place2 = models.CharField(max_length = 50)
    place3 = models.CharField(max_length = 50)
    sname = models.ForeignKey(station)

class junction(models.Model):
    sname = models.CharField(max_length = 50,primary_key = True)
    line1 = models.CharField(max_length = 15)
    line2 = models.CharField(max_length = 15)
    sname = models.ForeignKey(station)

