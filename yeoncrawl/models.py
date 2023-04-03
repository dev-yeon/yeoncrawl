from django.db import models


class Post(models.Model):
    std_img_url = models.CharField(max_length=300,null=True, blank=True)
    post_desc = models.TextField(null=True, blank=True)
    author_id = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=300,null=True, blank=True)
    like_count = models.IntegerField(null=True, blank=True)
    post_date = models.DateField(null=True, blank=True)
    img_list = models.ManyToManyField('PostImg',  blank=True)


class PostImg(models.Model):
    img_url = models.CharField(max_length=300,null=True, blank=True)
    img_alt = models.TextField(null=True, blank=True)
    img_name = models.CharField(max_length=100, null=True, blank=True)
    img_tag = models.CharField(max_length=100, null=True, blank=True)

