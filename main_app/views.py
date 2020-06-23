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

# --- PROFILE ROUTES --- #
@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts, 'user':request.user, 'profile': request.user.profile}
    return render(request, 'registration/profile.html',context)

@login_required
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

# --- CITIES ROUTES --- #
@login_required
def cities(request):
    cities = City.objects.all()
    context = { 'cities':cities}
    return render(request, 'cities/cities.html', context)

@login_required
def city_show(request, city_id):
    city = City.objects.get(id=city_id)
    current_user = request.user
    if request.method == "POST":
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            new_post_form=post_form.save(commit=False)
            new_post_form.city_id = city_id
            new_post_form.author_id = current_user.id
            new_post_form.save()
            return redirect('city_show', city_id=city_id)
    else:
        posts = Post.objects.filter(city=city_id)
    city_form = City_Form()
    context = {'city':city, 'posts':posts, 'city_form':city_form}
    return render(request, 'cities/city_show.html', context)

@login_required
def city_post_show(request, city_id, post_id):
    post = Post.objects.get(id=post_id)
    context={'post':post}
    return render(request, 'cities/show.html',context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
      edit_post_form = Edit_Post_Form(request.POST)
      if edit_post_form.is_valid():
        post.content = request.POST['content']
        post.title = request.POST['title']
        post.save()
        return redirect('city_post', city_id=post.city.id, post_id = post.id)
    else:
      edit_post_form = Edit_Post_Form(instance=post)
    context = {'edit_post_form': edit_post_form, 'post': post}
    return render(request, 'cities/edit.html', context)

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post_city= post.city.pk
    post.delete()
    return redirect('city_show',city_id=post_city)
