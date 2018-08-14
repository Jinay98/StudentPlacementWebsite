from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    UID = models.IntegerField(default=0)
    state = models.CharField(max_length=25, default='Maharashtra')
    city = models.CharField(max_length=20, default='Mumbai')
    branch = models.CharField(max_length=20, default='Computer')
    year = models.CharField(max_length=20, default='First year')

    def __str__(self):
        return self.user.username

class Company(models.Model):
    CID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    domain = models.CharField(max_length=20,default='')
    package=models.IntegerField(default=50000)
    pointer=models.FloatField(default=6.5)
    arrivaldate=models.DateField()

class Studmks(models.Model):
    UID=models.IntegerField(default=0,blank=True)
    s1 = models.FloatField(default=0)
    s2 = models.FloatField(default=0)
    s3 = models.FloatField(default=0)
    s4 = models.FloatField(default=0)
    s5 = models.FloatField(default=0)
    s5 = models.FloatField(default=0)
    s6 = models.FloatField(default=0)
    s7 = models.FloatField(default=0)
    s8 = models.FloatField(default=0)
    cgpa=models.FloatField(default=0.0)







