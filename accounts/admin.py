from django.contrib import admin
from accounts.models import Company,User,UserProfile
# Register your models here.

admin.site.register(UserProfile)
# admin.site.register(Student)
admin.site.register(Company)
#admin.site.register(Studentdetails)
# admin.site.register(StuAcads)