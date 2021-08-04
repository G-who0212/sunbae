from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)#Blog앱을 admin사이트에 등록을 시켜줌
admin.site.register(Comment)#Blog앱을 admin사이트에 등록을 시켜줌