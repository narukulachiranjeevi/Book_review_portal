from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class signUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','favorite_genres']


class UpdateUserForm(forms.ModelForm):
   class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
