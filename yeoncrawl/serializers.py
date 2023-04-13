from rest_framework import serializers
from .models import PostImg, Post


class PostImgSerializer(serializers.ModelSerializer):
    imageUrl = serializers.ImageField(label='프로필', source='image_url', use_url=True)
    class Meta:
        model = PostImg
        fields = ['img_url', 'img_alt', 'img_name', 'img_tag', 'imageUrl']


class PostSerializer(serializers.ModelSerializer):
    img_list = PostImgSerializer(many=True)

    class Meta:
        model = Post
        fields = ['post_desc', 'author_id', 'like_string', 'img_list', 'post_tag']
