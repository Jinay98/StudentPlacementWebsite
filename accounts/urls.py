from django.urls import path
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^$', views.home),
    url(r'login/$',login,{'template_name':'accounts/login.html'}),
    url(r'logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^Companies/$',views.company),
    #url(r'^Acads/$', views.acads),
    url(r'^Acads/$', views.index),
    #url(r'^register1/$',views.register1,name='register1')
    #url(r'add/$' ,views.addstudent),
    #url(r'home/$',login,{'template_name':'accounts/home.html'}),
]