from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post, Topic, Permission, User_Permissions, Post_UserReact, UserRelationship 

class CustomUserAdmin(UserAdmin):    
    model = CustomUser
    list_display = ['id','username']

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['id','topic','author', 'body']

class RelationAdmin(admin.ModelAdmin):
    model = UserRelationship
    list_display = ['id','follower','following']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
admin.site.register(Permission)
admin.site.register(User_Permissions)
admin.site.register(Post_UserReact)
admin.site.register(UserRelationship, RelationAdmin)