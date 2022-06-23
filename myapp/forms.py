from django import forms
from .models import  Profile,Companies,Rating,Review,Blog,Comment
from django.contrib.auth.models import User


class PostCompanyForm(forms.ModelForm):
    class Meta:
        model=Companies
        exclude = ('user','date')
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        exclude = ('user','date')        

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


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['company_culture', 'skill_development', 'work_life_balance','work_satisfaction','job_security','salary_benefits','career_growth']


class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        exclude = ('user_id','campany_id','created_at')


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		
		exclude = ['user','blog',]