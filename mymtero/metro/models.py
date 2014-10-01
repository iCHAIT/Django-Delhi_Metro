from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class stationinfo(models.Model):
    sid = models.IntegerField(primary_key = True)
    sname = models.CharField(max_length = 50, null = False)
    washroom = models.CharField(max_length = 5)
    parking = models.CharField(max_length = 5)
    elevator = models.CharField(max_length = 5)
    opening_date = models.DateField()
    contact = models.BigIntegerField()
    pincode = models.BigIntegerField(null = False)
    def __str__(self):
        return self.sname

class station(models.Model):
    statname = models.CharField(max_length = 50,null = False)
    line = models.CharField(max_length = 15,null = False)
    grade = models.CharField(max_length = 15,null = False)
    sid = models.ForeignKey('stationinfo',to_field = 'sid')
    def __str__(self):
        return self.statname


class places(models.Model):
    statname = models.CharField(max_length = 50,null = False)
    place = models.CharField(max_length = 75,null = False)
    sid = models.ForeignKey('stationinfo',to_field = 'sid')
    def __str__(self):
        return self.statname


class review(models.Model):
    statname = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    timest = models.DateTimeField()
    author = models.CharField(max_length = 50)
    bodytext = models.TextField()
    sid = models.ForeignKey('stationinfo',to_field = 'sid')
    def __str__(self):
        return self.sname

class validpath(models.Model):
    sid1 = models.IntegerField()
    sid2 = models.IntegerField()
    cost = models.IntegerField()

'''
class stationinfo(models.Model):
    sname = models.CharField(max_length = 50,primary_key = True)
    washroom = models.CharField(max_length = 5)
    parking = models.CharField(max_length = 5)
    elevator = models.CharField(max_length = 5)
    opening_date = models.DateField()
    contact = models.BigIntegerField()
    def __str__(self):
        return self.sname

class station(models.Model):
    sno = models.IntegerField()
    statname = models.CharField(max_length = 50,null = False)
    line = models.CharField(max_length = 15,null = False)
    pincode = models.BigIntegerField()
    grade = models.CharField(max_length = 15)
    sname = models.ForeignKey('stationinfo',to_field = 'sname')
    class Meta:
        unique_together = (('statname','line'))
    def __str__(self):
        return self.statname


class places(models.Model):
    statname = models.CharField(max_length = 50)
    place = models.CharField(max_length = 75)
    sname = models.ForeignKey('stationinfo',to_field = 'sname')
    def __str__(self):
        return self.statname


class junction(models.Model):
    statname = models.CharField(max_length = 50,primary_key = True)
    line1 = models.CharField(max_length = 15)
    line2 = models.CharField(max_length = 15)
    sname = models.ForeignKey('stationinfo',to_field = 'sname')
    def __str__(self):
        return self.statname


class review(models.Model):
    sname = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    timest = models.DateTimeField()
    author = models.CharField(max_length = 50)
    bodytext = models.TextField()
    def __str__(self):
        return self.sname

class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField()
    updated = models.DateTimeField()
'''





