from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Post, City, Profile
from .forms import Edit_Form, Post_Form, City_Form, Edit_Post_Form

# Create your views here.

# Define the home view
def home(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'home.html', context)

# --- Auth route --- #
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid signup please try again"
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'home.html', context)

def userlogin(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            login_error_message = "Invalid login please try again"
    else:
        form = UserCreationForm()
    context = {'form': form, 'login_error_message': login_error_message}
    return render(request, 'home.html', context)

# --- User routes --- #
@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts, 'user':request.user, 'profile': request.user.profile}
    return render(request, 'registration/profile.html',context)

def blog(request,blog_id):
    post = Post.objects.get(id=blog_id)
    context = {'post':post}
    return render(request, 'blog/show.html', context)

@login_required
def profile_edit(request, user_id):
    if request.method == 'POST':
      profile_form = Edit_Form(request.POST, instance= request.user.profile)
      if profile_form.is_valid():
          profile_form.save()
          return redirect('profile')
    else:
      profile_form = Edit_Form(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'blog/edit.html', context)

# --- PROFILE ROUTES --- #
""" def create_post(request, user_id):
    if request.method == 'POST':
        post_form = Post_Form(request.post, instance=request.user)
        if post_form.is_valid():
            post_form.save()
            return redirect('profile')
        else:
            post_form = Post_Form(instance = request.user)
    context = {'post_form': post_form}
    return render(request, 'registration/profile.html', context)
 """
# --- CITIES ROUTES --- #
def cities(request):
    cities = City.objects.all()
    context = { 'cities':cities}
    return render(request, 'cities/cities.html', context)

def city_show(request, city_id):
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id)
    context = {'city':city, 'posts':posts}
    return render(request, 'cities/city_show.html', context)

def city_post_show(request, city_id, post_id):
    post = Post.objects.get(id=post_id)
    context={'post':post}
    return render(request, 'cities/show.html',context)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
      edit_post_form = Edit_Post_Form(request.POST, instance= request.post_id)
      if edit_post_form.is_valid():
          edit_post_form.save()
          return redirect('city_post_show')
    else:
      edit_post_form = Edit_Post_Form(instance=request.post_id)
    context = {'edit_post_form': edit_post_form}
    return render(request, 'cities/edit.html', context)