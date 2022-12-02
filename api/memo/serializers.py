
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Post, Topic, Permission


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(min_length=4, max_length=15,required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    display = serializers.CharField(max_length=15, required=True)
    bio = serializers.CharField(max_length=200)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'display','bio')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('body', )

    def create(self):
        instance = self.Meta.model()
        instance.save()
        return instance
