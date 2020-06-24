from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Post, City, Profile

admin.site.register(Post)
admin.site.register(City)
admin.site.register(Profile)