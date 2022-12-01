from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display = models.CharField(max_length=30, null=True, unique=True)
    bio = models.CharField(max_length=255, null=True)
    # pfp = models.ImageField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
"""  

Atts need to be added to model field types.

"""
class Post(models.Model):
    created = models.DateTimeField(auto_now=True)
    # updated = models.DateTimeField(auto_now_add=True)
    # status = models.CharField()
    # like = models.IntegerField()
    # dislike = models.IntegerField()
    def __str__(self):
        return f"{self.created}"

class Topic(models.Model):
    categories = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.categories}"

class Permission(models.Model):
    role = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.role}"

