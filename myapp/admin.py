from django.contrib import admin

from .models import Profile, Companies,Review,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Companies)
admin.site.register(Review)
admin.site.register(Comment)