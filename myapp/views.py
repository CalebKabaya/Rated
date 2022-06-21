from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from .models import Profile,Companies,Rating

from django.contrib.auth import login,authenticate,logout
from .forms import  UpdateUserForm, UpdateUserProfileForm,PostCompanyForm,RatingsForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
# Create your views here.
def index(request):
    all_post=Companies.objects.all()
    all_post=all_post[::-1]
    return render(request,'index.html',{"all_post":all_post})    

 

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



@login_required(login_url='/accounts/login/')
def postcompany(request):
    if request.method == 'POST':
        form = PostCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=request.user
            project.save()
            
        return redirect('/')
    else:
        form = PostCompanyForm()
    try:
        posts=Companies.objects.all() 
        posts=posts[::-1]
    except Companies.DoesNotExist:
        posts=None

    context = {
        'form':form,
    }
    return render(request, 'addpost.html', context)

@login_required(login_url='login')
def project(request,post_id):
    company = Companies.objects.get(id=post_id)
    ratings = Rating.objects.filter(user=request.user, id=post_id).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.company = company
            rate.save()
            post_ratings = Rating.objects.filter(company=company)

            company_culture_ratings = [camp.company_culture for camp in post_ratings]
            company_culture_average = sum(company_culture_ratings) / len(company_culture_ratings)

            skill_development_ratings = [dev.skill_development for dev in post_ratings]
            skill_development_average = sum(skill_development_ratings) / len(skill_development_ratings)

            work_life_balance_ratings = [work.work_life_balance for work in post_ratings]
            work_life_balance_average = sum(work_life_balance_ratings) / len(work_life_balance_ratings)


            work_satisfaction_ratings = [sat.work_satisfaction for sat in post_ratings]
            work_satisfaction_average = sum(work_satisfaction_ratings) / len(work_satisfaction_ratings)


            job_security_ratings = [job.job_security for job in post_ratings]
            job_security_average = sum(job_security_ratings) / len(job_security_ratings)


            salary_benefits_ratings = [content.salary_benefits for content in post_ratings]
            salary_benefits_average = sum(salary_benefits_ratings) / len(salary_benefits_ratings)


            job_security_ratings = [content.job_security for content in post_ratings]
            job_security_average = sum(job_security_ratings) / len(job_security_ratings)


            career_growth_ratings = [car.career_growth for car in post_ratings]
            career_growth_average = sum( career_growth_ratings) / len(career_growth_ratings)

            score = (company_culture_average + skill_development_average + work_life_balance_average + work_satisfaction_average + job_security_average + salary_benefits_average  + career_growth_average) / 7
            print(score)
            rate.company_culture_average = round(company_culture_average, 2)
            rate.skill_development_average = round(skill_development_average, 2)
            rate.work_life_balance_average = round(work_life_balance_average, 2)
            rate.work_satisfaction_average = round(work_satisfaction_average, 2)
            rate.job_security_average = round(job_security_average, 2)
            rate.salary_benefits_average = round(salary_benefits_average, 2)
            rate.career_growth_average = round(career_growth_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'company': company,
        'form': form,
        'rating_status': rating_status

    }
    return render(request, 'singlecompany.html', params)