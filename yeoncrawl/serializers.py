from rest_framework import serializers
from .models import PostImg, Post


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImg
        fields = ['img_url', 'img_alt', 'img_name', 'img_tag']


class PostSerializer(serializers.ModelSerializer):
    img_list = PostImgSerializer(many=True)

    class Meta:
        model = Post
        fields = ['post_desc', 'author_id', 'like_string', 'img_list', 'post_tag']
