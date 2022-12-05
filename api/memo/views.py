from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from django_filters.rest_framework import DjangoFilterBackend

from .models import CustomUser, Post, Topic, UserRelationship

from .serializers import CustomUserSerializer, PostSerializer, TopicSerializer, UserRelationshipSerializer, UserPostSerializer, UserPostSerializer, UserFollowerSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# User can create a Post
class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# A view list of all posts that are not in responses to any other post AKA a comment
# FilterPosts class allows for filtering of Posts based on response_to column data
# To filter Main Posts ?response_to__isnull=True

# To filter Comments of a Post ?response_to=*id of post
class FilterPosts(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'response_to':['exact', 'isnull']}

# ?username=admin
class FilterUserName(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

class FilterFollower(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['follower']


# Not currently used replaced with UserPost
class FilterUserPosts(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']


# Nested json get post with username test
class UserPost(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']



class UserList(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

class RelationshipList(ModelViewSet):
    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostList(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


#User can get a list of topics from postgres DB
class TopicList(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post']

    @classmethod
    def get_as_view(cls):
        return cls.as_view({'get': 'list','post':'create'}) # as_views CRUD functions moved from ulrs to views example


