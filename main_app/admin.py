from django.contrib import admin

# Register your models here.
from .models import Post, City, Profile

admin.site.register(Post)
admin.site.register(City)
admin.site.register(Profile)