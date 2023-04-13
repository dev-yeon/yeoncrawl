import hashlib
import base64
from django.db import models
import random
import os
import datetime


def user_directory_path(instance, filename):
    now = datetime.datetime.now()
    path = "{date}/{filename}".format(date=str(now.date()), filename=filename,)
    return path


class Post(models.Model):
    std_img_url = models.CharField(max_length=300,null=True, blank=True)
    post_desc = models.TextField(null=True, blank=True)
    author_id = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=300,null=True, blank=True)
    like_count = models.IntegerField(null=True, blank=True)
    like_string = models.CharField(max_length=100, null=True, blank=True)
    post_date = models.DateField(null=True, blank=True)
    img_list = models.ManyToManyField('PostImg',  blank=True)
    post_tag = models.CharField(max_length=100, blank=True, null=True)


class PostImg(models.Model):
    img_url = models.CharField(max_length=300,null=True, blank=True)
    image_url = models.ImageField(blank=True, null=True, upload_to=user_directory_path)
    img_alt = models.TextField(null=True, blank=True)
    img_name = models.CharField(max_length=100, null=True, blank=True)
    img_tag = models.CharField(max_length=100, null=True, blank=True)

