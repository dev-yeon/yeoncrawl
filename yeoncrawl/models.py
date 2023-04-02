from django.db import models


class Post(models.Model):
    std_img_url = models.CharField(max_length=300)
    post_desc = models.TextField()
    author_id = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    like_count = models.IntegerField()
    post_date = models.DateField()
    img_list = models.ManyToManyField('PostImg')


class PostImg(models.Model):
    img_url = models.CharField(max_length=300)
    img_alt = models.TextField()
    img_name = models.CharField(max_length=100, null=True, blank=True)

