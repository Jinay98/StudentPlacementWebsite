from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    last_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    email = forms.EmailField(max_length=254, help_text='Required.Enter a valid email address.')
    City = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    State = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    UID = forms.IntegerField(required=True, help_text='Compulsory Field')
    Branch = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    Year = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2' )

        # model = UserProfile
        # fields = ('UID','first_name', 'State', 'City','Branch','Year', 'password1',)

class UserProfileForm(forms.ModelForm):
    #Name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    #last_name = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    City = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    State = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    UID = forms.IntegerField(required=True, help_text='Compulsory Field',)
    Branch = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    Year = forms.CharField(max_length=10, required=True, help_text='Compulsory Field')
    Password = forms.CharField(max_length=30, required=True, help_text='Compulsory Field')
    class Meta:
         model = UserProfile
         fields = ('UID', 'State', 'City','Branch','Year', 'Password',)

