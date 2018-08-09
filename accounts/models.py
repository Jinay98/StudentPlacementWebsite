from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # description = models.CharField(max_length=100 , default='')
    # city = models.CharField(max_length=100,default='')
    # website = models.CharField(max_length=100,default='')
    # phone = models.IntegerField(default=0)
    #username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+',default='jinay1')
    UID = models.IntegerField(default=0)
    name = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=20, default='')
    branch = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=15, default='12345six')
    s1 = models.FloatField(default=0)
    s2 = models.FloatField(default=0)
    s3 = models.FloatField(default=0)
    s4 = models.FloatField(default=0)
    s5 = models.FloatField(default=0)
    s5 = models.FloatField(default=0)
    s6 = models.FloatField(default=0)
    s7 = models.FloatField(default=0)
    s8 = models.FloatField(default=0)
    cgpa = models.FloatField(default=0)


class Company(models.Model):
    CID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    domain = models.CharField(max_length=20,default='')
    package=models.IntegerField(default=50000)
    pointer=models.FloatField(default=6.5)
    arrivaldate=models.DateField()
    

# class StuAcads(models.Model):
#     UID=models.OneToOneField(UserProfile,on_delete=models.CASCADE)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)




# class Student(models.Model):
#     UID=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=20,default='')
#     state = models.CharField(max_length=25, default='')
#     city = models.CharField(max_length=20, default='')
#     branch = models.CharField(max_length=20, default='')
#     year = models.CharField(max_length=20, default='')
#     password=models.CharField(max_length=15,default='12345six')


# class Studentdetails:
#     UID = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20, default='')
#     state = models.CharField(max_length=25, default='')
#     city = models.CharField(max_length=20, default='')
#     branch = models.CharField(max_length=20, default='')
#     year = models.CharField(max_length=20, default='')





