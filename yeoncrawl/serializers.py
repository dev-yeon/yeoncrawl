from rest_framework import serializers
from .models import PostImg


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImg
        fields = ['img_url', 'img_alt', 'img_name', 'img_tag']