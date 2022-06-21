from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth import login,authenticate,logout
from .forms import  UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('/register')
        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1,
        ) 
        new_user.save() 
        return render (request,'login.html')
    return render(request,'register.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)

def profile(request):
    user=request.user
    my_profile=Profile.objects.get(user=user)
    return render(request,"profile.html",{'my_profile':my_profile,"user":user})
@login_required(login_url='login')
def update_profile(request):
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            # return HttpResponseRedirect(request.path_info)
            return redirect('profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    contex = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'update.html', contex)    