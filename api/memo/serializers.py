
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Post, Topic, Permission, User_Permissions, Post_UserReact, UserRelationship


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(min_length=4, max_length=15,required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    display = serializers.CharField(max_length=15, required=False)
    bio = serializers.CharField(max_length=200, required=False)
    
    class Meta:
        model = CustomUser
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=False)
    username = serializers.CharField(min_length=4, max_length=15,required=False)
    class Meta:
        model = CustomUser
        fields = ('__all__')
    

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('__all__')

    def create(self,validated_data):
        return Post.objects.create(**validated_data)

# TopicSerializer is working 
class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ('categories',)

class UserRelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRelationship
        fields = ("__all__")
        


# Testing nested json, username to show in posts instead of [fk] CustomUser id
class UserPostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    topic = TopicSerializer()

    class Meta:
        model = Post
        fields = ('id','created','body','like','dislike','author','topic','response_to')

class UserFollowerSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer()
    following = CustomUserSerializer()

    class Meta:
        model = UserRelationship
        fields = ['follower','following']


    
