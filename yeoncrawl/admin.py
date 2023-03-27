from django.contrib import admin

from yeoncrawl.models import Post, PostImg

class PostAdmin(admin.ModelAdmin):
    pass

class PostImgAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PostImg, PostImgAdmin)
