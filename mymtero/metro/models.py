from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class stationinfo(models.Model):
    CHOICES = (
        ('Yes','Yes'),
        ('No','No'),
    
    )
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    washroom = models.CharField(max_length = 5,choices = CHOICES)
    parking = models.CharField(max_length = 5,choices = CHOICES)
    elevator = models.CharField(max_length = 5,choices = CHOICES)
    opening_date = models.DateField()
    contact = models.BigIntegerField()
    pincode = models.BigIntegerField()
    cost = models.IntegerField()
    pathid = models.IntegerField()
    calculated = models.IntegerField()
    def __str__(self):
        return self.sname

class station(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    line = models.CharField(max_length = 15)
    grade = models.CharField(max_length = 15)
    def __str__(self):
        return self.sname


class places(models.Model):
    pid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    place = models.CharField(max_length = 75)
    def __str__(self):
        return self.sname


class path(models.Model):
    pathid = models.AutoField(primary_key=True)
    fromsid = models.ForeignKey(stationinfo, related_name = 'fromsid_set')
    tosid = models.ForeignKey('stationinfo', related_name = 'tosid_set')
    cost = models.IntegerField()




class review(models.Model):
    rid = models.AutoField(primary_key = True)
    sname = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    timest = models.DateTimeField()
    bodytext = models.TextField()
    def __str__(self):
        return self.sname




