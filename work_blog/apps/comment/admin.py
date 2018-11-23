from django.contrib import admin

from comment.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_object', 'text', 'comment_time', 'user', 'root', 'parent', 'reply_to']

admin.site.register(Comment, CommentAdmin)