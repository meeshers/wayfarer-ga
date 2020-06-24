from django.forms import ModelForm
from django import forms
from .models import Post, Profile, City

class Post_Form(ModelForm):
  class Meta:
    model = Post
    fields = ['title','content']

class Edit_Form(ModelForm):
  class Meta:
    model = Profile
    fields = ['name','city']

class City_Form(ModelForm):
  class Meta:
    model = City
    fields = ['name']

class Edit_Post_Form(ModelForm):
  class Meta:
    model = Post
    fields=['title','content']

