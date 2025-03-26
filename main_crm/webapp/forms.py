from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,PasswordInput
from .models import *

# register
class createuserform(UserCreationForm):
    class meta:
        model = User
        fields = ['username','password1','password2']

# login 
class loginform(AuthenticationForm) :
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


# employee
class create_employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name','email','phone']

# customer
class create_customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'status']

# activity
class create_activity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['customer', 'employee', 'activity_type', 'note']

# activity type
class create_activitytype(forms.ModelForm):
    class Meta:
        model = Activity_type
        fields = ['type_name']

# update activity
class update_activity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['customer', 'employee', 'activity_type', 'note']