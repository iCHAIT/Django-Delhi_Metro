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
    cost = models.CharField(max_length = 5,null=True,blank=True)
    pathid = models.CharField(max_length = 5,null=True,blank=True)
    calculated = models.CharField(max_length = 5,null=True,blank=True)
    def __str__(self):
        return self.sname
    class Meta:
        verbose_name_plural = "Station Information"


class station(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    line = models.CharField(max_length = 15)
    grade = models.CharField(max_length = 15)
    sid = models.ForeignKey('stationinfo', to_field = 'sid')
    def __str__(self):
        return self.sname
    class Meta:
        verbose_name_plural = "Station"


class places(models.Model):
    pid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    place = models.CharField(max_length = 75)
    sid = models.ForeignKey('stationinfo', to_field = 'sid')
    def __str__(self):
        return self.sname
    class Meta:
        verbose_name_plural = "Places"


class path(models.Model):
    pathid = models.AutoField(primary_key=True)
    fromsid = models.ForeignKey('stationinfo', related_name = 'fromsid_set')
    tosid = models.ForeignKey('stationinfo', related_name = 'tosid_set')
    cost = models.IntegerField()
    def __int__(self):
        return self.pathid
    class Meta:
        verbose_name_plural = "Path"


class review(models.Model):
    CHOICES = (
               ('Yes','Yes'),
               ('No','No'),
               
               )
    rid = models.AutoField(primary_key = True)
    sname = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    timest = models.DateTimeField()
    bodytext = models.TextField()
    approved = models.CharField(max_length = 5)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Review"


class dir(models.Model):
    CHOICES = (
                ('KM', 'Khan Market'),
                ('KG', 'Kashmere Gate'),
               
        )
    source = models.CharField(max_length = 50,choices = CHOICES)
    dest = models.CharField(max_length = 50)


class info(models.Model):
    sname = models.CharField(max_length = 50)


class near1(models.Model):
    place = models.CharField(max_length = 75)

class near2(models.Model):
    pin = models.BigIntegerField()


class rev1(models.Model):
    sname = models.CharField(max_length = 50)

class rev2(models.Model):
    sname = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    bodytext = models.TextField()
    author = models.CharField(max_length = 50)

