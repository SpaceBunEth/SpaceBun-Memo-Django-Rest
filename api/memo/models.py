from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display = models.CharField(max_length=30, null=True, unique=True)
    bio = models.CharField(max_length=255, null=True)
    # pfp = models.ImageField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Post():
    
    pass

class Topic():
    pass

class Permission():
    pass

