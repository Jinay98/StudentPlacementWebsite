from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import loader
from accounts.forms import SignUpForm
#from accounts.forms import SignUpForm,UserProfileForm
from .models import Company
# Create your views here.
def home(request):
    numbers=[1,2,3,4,5]
    name = "Jinay Parekh"
    args={'myname':name,'numbers':numbers}
    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
            #return HttpResponseRedirect('/accounts/')

    else:
        form=UserCreationForm()
        args={'form':form}
        #args={}
        #args['form']= form
        return render(request , 'accounts/reg_form.html',args)



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #form1 =UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

#             obj = UserProfile()
#             obj.user_id = request.user.id
#             obj.Name = request.POST.get('first_name', '') + " " + request.POST.get('last_name', '')
#             print("name is "+obj.Name)
#
#             obj.UID = request.POST.get('UID')
#             print("UID is " + obj.UID)
#             obj.name = request.POST.get('City', '')
#             obj.state = request.POST.get('State', '')
#             obj.password = request.POST.get('password1', '')
#             obj.branch = request.POST.get('Branch', '')
#             obj.year = request.POST.get('Year', '')
#             obj.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/accounts')
    else:
        form = SignUpForm()
#         # obj = UserProfile()
#         # obj.user_id = request.user.id
#         # obj.name = request.POST.get('first_name','')+" "+request.POST.get('last_name','')
#         # obj.UID = request.POST.get('UID')
#         # obj.city = request.POST.get('City','')
#         # obj.state = request.POST.get('State','')
#         # obj.password = request.POST.get('password1','')
#         # obj.branch = request.POST.get('Branch','')
#         # obj.year = request.POST.get('Year','')
#         # obj.save()
    return render(request, 'accounts/signup.html', {'form': form})

# def addstudent(request):
#     if request.method=='POST':
#         obj = UserProfile()
#         obj.name =request.POST.get('name','')
#         obj.UID = request.POST.get('UID','')
#         obj.city=request.POST.get('city','')
#         obj.state=request.POST.get('state','')
#         obj.password=request.POST.get('password','')
#         obj.branch=request.POST.get('branch','')
#         obj.year=request.POST.get('year','')
#         obj.save()
#     return render(request, 'accounts/home.html')

def company(request):
    return render( request,'accounts/company.html')

def acads(request):
    return render( request,'accounts/acads.html')

# def addstudentacads(request):
#     if request.method=='POST':
#         obj = UserProfile()
#         obj.s1 =request.POST.get('s1','')
#         obj.s2 = request.POST.get('s2','')
#         obj.s3=request.POST.get('s3','')
#         obj.s4=request.POST.get('s4','')
#         obj.s5=request.POST.get('s5','')
#         obj.s6=request.POST.get('s6','')
#         obj.s7=request.POST.get('s7','')
#         obj.s8=request.POST.get('s8','')
#         obj.cgpa=(float(obj.s1)+float(obj.s2)+float(obj.s3)+float(obj.s4)+float(obj.s5)+float(obj.s6)+float(obj.s7)+float(obj.s8))/8
#         obj.save()
#     return render(request, 'accounts/home.html')
#
# def checkeligibility(request):
#     obj = UserProfile()
#     obj1=Company()
#     if(float(obj.cgpa) >=obj1.pointer):
#         return "YES"
#     else:
#         return "NO"
    # template = loader.get_template('articles/index.html')
    # context = {
    #     'new_article_id': article.pk,
    # }
    # return HttpResponse(template.render(context, request))
# def displayCompany(self,request):
#     pos




def index(request):
    UID= request.POST.get('UID')

    stuname = request.POST.get('stuname')

    city = request.POST.get('city')

    state = request.POST.get('state')
    branch = request.POST.get('branch')
    year=request.POST.get('year')
    submitbutton = request.POST.get('Submit')
    #print(state+branch+UID+stuname+year)
    context = {'UID': UID, 'stuname': stuname,
               'city': city, 'state': state,
               'branch':branch,'year': year,
               'submitbutton': submitbutton}

    return render(request, 'accounts/acads.html', context)



