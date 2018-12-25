from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog, BlogType, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'date_joined')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    blogtype = BlogTypeSerializer(read_only=True)
    tags = TagSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Blog
        exclude = ('content',)