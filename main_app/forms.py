from django.forms import ModelForm
from django import forms
from .models import Post, Profile

class Post_Form(ModelForm):
  class Meta:
    model = Post
    fields = ['title','content']

class Edit_Form(ModelForm):
  class Meta:
    model = Profile
    fields = ['name','city']


class LoginForm(forms.Form):
    login_form = forms.CharField(label="Login Form", max_length=100)
