from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/<int:user_id>/edit/',views.profile_edit, name='edit'),
    path('accounts/profile/<int:blog_id>/', views.blog, name='blog'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>', views.city_show, name='city_show'),
    path('cities/<int:city_id>/<int:post_id>', views.city_post_show, name="city_post"),
    path('cities/<int:post_id>/edit', views.edit_post, name="edit_post")
]

