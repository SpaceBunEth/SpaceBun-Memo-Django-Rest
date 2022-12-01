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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    like = models.IntegerField(null=True)
    dislike = models.IntegerField(null=True)
    topic = models.OneToOneField('Topic', on_delete=models.CASCADE, primary_key=True, default=1) # One Topic id/category to One Post
    def __str__(self):
        return f"{self.body}"

class Topic(models.Model):
    categories = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.categories}"

class Permission(models.Model):
    role = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.role}"

class Post_UserReact(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE) # ManyToOne relationship using Foreign Key
    post_info = models.ForeignKey('Post', on_delete=models.CASCADE)
    # topic_type = models.OneToOneField('Topic', on_delete=models.CASCADE, primary_key=True,)
    liked = models.BooleanField()
    disliked = models.BooleanField()
    # comment = models.CharField(max_length=200)
