from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_picture=CloudinaryField('image')
    bio=models.TextField(max_length=500,default="My Bio",blank=True)
    name=models.CharField(max_length=120,blank=True)
    location=models.CharField(max_length=100,blank=True)
    contact_email=models.EmailField(max_length=100,blank=True)

    def __str__(self):
        return f'{self.user.username}Profile'
    @receiver(post_save,sender=User) 
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User) 
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
        
# class Category(models.Model):
#     category_name=models.CharField(max_length=30,unique=True)

#     def __str__(self):
#         return self.category_name

#     def save_category(self):
#         self.save 
#     def delete_category(self):
#         self.delete   

class Companies(models.Model):
    name=models.CharField(max_length=160)
    website=models.URLField(max_length=300)
    about=models.TextField(max_length=300)
    size=models.IntegerField(null=True)
    logo=CloudinaryField('image')
    location=models.CharField(max_length=100,blank=True)
    # camp_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'{self.name}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()


    @classmethod
    def search_company(cls,name):
        return cls.objects.filter(name__icontains=name).all()  

    

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    company_culture = models.IntegerField(choices=rating, default=0, blank=True)
    skill_development = models.IntegerField(choices=rating, blank=True)
    work_life_balance = models.IntegerField(choices=rating, blank=True)
    work_satisfaction = models.IntegerField(choices=rating, blank=True)
    job_security = models.IntegerField(choices=rating, blank=True)
    salary_benefits = models.IntegerField(choices=rating, blank=True)
    career_growth = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    company_culture_average = models.FloatField(default=0, blank=True)
    skill_development_average = models.FloatField(default=0, blank=True)
    work_life_balance_average = models.FloatField(default=0, blank=True)
    work_satisfaction_average = models.FloatField(default=0, blank=True)
    job_security_average = models.FloatField(default=0, blank=True)
    salary_benefits_average = models.FloatField(default=0, blank=True)
    career_growth_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.company} Rating'

class Review(models.Model):
    policy = (
        (1, 'Permanent work from home'),
        (2, 'Working from office'),
        (3, 'Hybrid (working from office & home)'),
        (4, 'Unclear at the moment'),
    )
    department = models.CharField(max_length=120)
    job_title = models.CharField(max_length=254)
    pros= models.TextField(blank=True)
    cons = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    work_enviroment=models.IntegerField(choices=policy, default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    campany_id= models.ForeignKey(Companies,on_delete=models.CASCADE ,related_name='campany')

    def __str__(self):
        return f'{self.comment} Review'

    def create_review(self):
        self.save()

    def delete_review(self):
        self.delete()

class Blog(models.Model):
    title=models.CharField(max_length=160)
    article=models.TextField()
    blog_image=CloudinaryField('image')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog')
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'{self.title}'

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()

    @classmethod
    def all_blogs(cls):
        return cls.objects.all()


    @classmethod
    def search_blog(cls,title):
        return cls.objects.filter(title__icontains=title).all()  

class Comment(models.Model):
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        comments = models.TextField(max_length=160)

        def __str__(self):
            return self.comments

        def save_comment(self):
            self.save()

        def delete_comment(self):
            self.delete()


class Likes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    blog_id= models.ForeignKey(Blog,on_delete=models.CASCADE)