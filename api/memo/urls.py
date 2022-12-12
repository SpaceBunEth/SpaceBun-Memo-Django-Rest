from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    
    # Update one user by ID
    path('userupdate/<int:pk>/', UserUpdate.as_view({'get':'retrieve','put':'update'}), name="user-update"),
    
    path('users/list/', UserList.as_view({'get': 'list'}), name="user_list"),

    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('posts/', PostList.as_view({'get': 'list'}), name="get_post_list"), #get a list of all posts

    path('topics/', TopicList.get_as_view(), name='get_topics_list'),


    # Get and Post relationships
    path('follow/', RelationshipList.as_view({'get':'list','post':'create','delete':'destroy'}), name="user_relationship_list"),
    # Delete Relationships 
    path('removefollow/<int:pk>/', RelationshipList.as_view({'delete':'destroy'}), name="remove_follow"),



    #Posts that are not comments
    #?response_to__isnull=True
    path('timeline/',FilterPosts.as_view(), name="timeline_posts"),
    
    # Filter Comments to a post with json nested user info
    path('comments/',FilterComments.as_view(), name="comment_posts"),

    # ?search="username"
    path('searchuser/',SearchUserName.as_view(), name="search_user"),

    path('username/',FilterUserName.as_view(), name="filter_by_username"),

    path('createpost/',CreatePost.as_view(), name="create_posts"),

    #path('userposts/',UserPosts.as_view(), name="filter_posts_by_user_id")
    path('userposts/',UserPost.as_view(), name="filter_posts_by_user_id"),
    path('userpostsrecent/',UserPostRecent.as_view(), name="filter_posts_by_user_id"),
    
    

    #user's list of followers
    path('follower/', FilterFollower.as_view(), name="user_follower_list"),
    #user's list of following
    path('following/', FilterFollowing.as_view(), name="user_follower_list")



]
