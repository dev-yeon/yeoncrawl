# Generated by Django 4.1.7 on 2023-04-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("yeoncrawl", "0002_post_like_string"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_tag",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]