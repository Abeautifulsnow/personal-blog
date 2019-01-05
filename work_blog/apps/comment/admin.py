from django.contrib import admin
from django.utils.safestring import mark_safe
from comment.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_object', 'safe_text', 'comment_time', 'user', 'safe_root', 'safe_parent', 'reply_to']

    def safe_text(self, obj):
        return mark_safe(obj.text)
    safe_text.short_description = '评论内容'

    def safe_root(self, obj):
        return mark_safe(obj.root)
    safe_root.short_description = '根评论'
    
    def safe_parent(self, obj):
        return mark_safe(obj.root)
    safe_parent.short_description = '父评论'


admin.site.register(Comment, CommentAdmin)