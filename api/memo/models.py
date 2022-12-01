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
class Post():
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.CharField()
    like = models.IntegerField()
    dislike = models.IntegerField()


class Topic():
    categories = models.CharField()


class Permission():
    role = models.CharField()


