from django.contrib import admin

from .models import Profile, Companies

# Register your models here.
admin.site.register(Profile)
admin.site.register(Companies)
# admin.site.register(Category)