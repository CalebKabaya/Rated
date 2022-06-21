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