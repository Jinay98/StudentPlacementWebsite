from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import loader
from accounts.forms import SignUpForm,UserProfileForm
#from accounts.forms import SignUpForm,UserProfileForm
from .models import Company,UserProfile,Studmks
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
# Create your views here.
def home(request):
    numbers=[1,2,3,4,5]
    name = "Jinay Parekh"

    obj = UserProfile.objects.get(user_id=request.user.id)
    args = {'UID': obj.UID, 'state': obj.state,'city':obj.city,'branch':obj.branch,'year':obj.year}
    return render(request,'accounts/home.html',args)



# def register(request):
#     if request.method == "POST":
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/')
#             #return HttpResponseRedirect('/accounts/')
#
#     else:
#         form=UserCreationForm()
#         args={'form':form}
#         #args={}
#         #args['form']= form
#         return render(request , 'accounts/reg_form.html',args)



def register(request):
    print('Hello')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print('Hello')
        #form1 =UserProfileForm(request.POST)
        #profile_form = UserProfileForm(request.POST, instance=request.user.id)
        if form.is_valid():
            objuser = form.save()
            #profile_form.save()

            #ediitedd
            print(objuser.id)


            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #obj1=User()
            #obj = UserProfile.objects.get(user_id=31)
            print(request.user.id)
            #obj=UserProfile.objects.get(user_id=objuser.id)


            objt = UserProfile(user=objuser, UID=request.POST.get('UID'), state=request.POST.get('State'),
                              city=request.POST.get('City'), branch=request.POST.get('Branch'),
                              year=request.POST.get('Year'))

            print(objt)

            objt.save()

            # user = User.objects.get(pk=8)
            # user.UserProfile.UID=1010101
            # user.UserProfile.city='Delhi'
            # user.save()


            # user = User.objects.get(username=request.user.username)
            # user.UserProfile.UID = 100
            # user.UserProfile.s1=9.6
            # user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/accounts')

    else:
        form = SignUpForm()

    print('Hello')
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def company(request):
    # entry_list = Company.objects.all()
    # print(entry_list.CID)
    # return render(request,'accounts/company.html',entry_list)
    obj = UserProfile.objects.get(user_id=request.user.id)
    print(obj.UID)
    obj1=Studmks.objects.get(UID=obj.UID)
    print(obj1.cgpa)
    result = Company.objects.values()


    return render(request,'accounts/company.html',{'result':result,'UID':obj.UID,'cgpa':obj1.cgpa})

@login_required()
def acads(request):
    return render( request,'accounts/acads.html')


@login_required
def index(request):
    UID= request.POST.get('UID')
    # cgpa=0
    obj=Studmks()
    s1 = request.POST.get('s1')
    print(s1)
    s2 = request.POST.get('s2')
    s3 = request.POST.get('s3')
    s4 = request.POST.get('s4')
    s5 = request.POST.get('s5')
    s6 = request.POST.get('s6')
    s7 = request.POST.get('s7')
    s8 = request.POST.get('s8')
    submitbutton = request.POST.get('Submit')
    dbsavebtn=request.POST.get('DBstore')
    print(dbsavebtn)

    if submitbutton=='Submit':
        cgpa=calc(s1,s2,s3,s4,s5,s6,s7,s8)
        print(cgpa)
    else:
        cgpa=0.0
    if dbsavebtn == 'Save To DB':
        obj.UID=int(UID)
        obj.s1 = float(s1)
        obj.s2 = float(s2)
        obj.s3 = float(s3)
        obj.s4 = float(s4)
        obj.s5 = float(s5)
        obj.s6 = float(s6)
        obj.s7 = float(s7)
        obj.s8 = float(s8)
        cgpa = calc(s1, s2, s3, s4, s5, s6, s7, s8)
        obj.cgpa = float(cgpa)
        obj.save()

    context = {'UID': UID, 's1': s1,
                's2': s2, 's3': s3,
                's4':s4,'s5': s5,'s6':s6,
                's7':s7,'s8':s8,'cgpa':cgpa,
                'submitbutton': submitbutton}

    return render(request, 'accounts/acads.html', context)



@login_required
def profile(request):
    args={'user':request.user}
    return render(request,'accounts/home.html',args)

def calc(s1,s2,s3,s4,s5,s6,s7,s8):
    count=0
    if float(str(s1))!=0:
        count+=1
    if float(str(s2))!=0:
        count+=1
    if float(str(s3))!=0:
        count+=1
    if float(str(s4))!=0:
        count+=1
    if float(str(s5))!=0:
        count+=1
    if float(str(s6))!=0:
        count+=1
    if float(str(s7))!=0:
        count+=1
    if float(str(s8))!=0:
        count+=1
    cgpa=(float(str(s1))+float(str(s2))+float(str(s3))+float(str(s4))+float(str(s5))+float(str(s6))+float(str(s7))+float(str(s8)))/float(count)
    print("count is ="+(str(count)))
    return cgpa




