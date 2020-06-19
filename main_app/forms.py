from django.forms import ModelForm
from .models import Post, Profile

class Post_Form(ModelForm):
  class Meta:
    model = Post
    fields = ['title','content']

""" class Edit_Form(ModelForm):
  class Meta:
    model = Profile
    fields = ['city'] """