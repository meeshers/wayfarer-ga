from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=250)
  city = models.ForeignKey(City, on_delete = models.CASCADE, null=True)
  def __str__(self):
    return f'Title: {self.title} in {self.city}'

# extending User model to have city/date
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=100, null=True)

  def __str__(self):
    return f'{self.user}: {self.city}' 

# signals so that Profile model will create/update when User is updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save





