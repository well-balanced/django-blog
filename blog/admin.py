from django.contrib import admin
from .models import Post, Comment
from django.utils import timezone

admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
