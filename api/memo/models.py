from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display = models.CharField(max_length=30, null=True, unique=True)
    bio = models.CharField(max_length=255, null=True)
    pfp = models.URLField(max_length=200, null=True)


    def __str__(self):
        return f"{self.username} {self.display} {self.email}"

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    like = models.IntegerField(null=True, default=0)
    dislike = models.IntegerField(null=True, default=0)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True, blank=True) # One Topic id/category to One Post
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True) #recursive relationship, for creating comments
    def __str__(self):
        return f"{self.topic} {self.author}"

class Topic(models.Model):
    categories = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.categories}"

class Permission(models.Model):
    role = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.role}"


# Pivot table for CustomeUser and Permission types ex, Admin, Mod, User, AnonUser
class User_Permissions(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='user_permission')
    permission_type = models.ForeignKey('Permission', on_delete=models.CASCADE, related_name='permission_type')

# Pivot table for CustomUser and Post Table
class Post_UserReact(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE) # ManyToOne relationship using Foreign Key
    post_info = models.ForeignKey('Post', on_delete=models.CASCADE)

    # topic_type = models.OneToOneField('Topic', on_delete=models.CASCADE, primary_key=True,)

    liked = models.BooleanField()
    disliked = models.BooleanField()

    # comment = models.CharField(max_length=200)

# CustomUser relations Table, (who follows who?)
class UserRelationship(models.Model):
    follower = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='user_follower')
    following = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='user_following')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["follower","following"], name='unique_follow')
        ]