from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Post, City, Profile

admin.site.register(Post)
admin.site.register(City)

# define inline admin for profile model
class ProfileInLine(admin.StackedInline):
  model = Profile
  can_delete = False
  verbose_name_plural = 'profile'

# Define new User Admin
class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)