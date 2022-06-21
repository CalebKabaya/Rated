from django import forms
from .models import  Profile
from django.contrib.auth.models import User




class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=254,help_text='Required.Inform a valid email addres')
    class Meta:
        model= User
        fields=('username','email')

class UpdateUserProfileForm(forms.ModelForm):
    email=forms.EmailField(max_length=254,help_text='Required.Inform a valid email addres')
    class Meta:
        model= Profile
        fields=('name','bio','profile_picture','location','contact_email')
