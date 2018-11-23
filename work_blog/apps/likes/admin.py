from django.contrib import admin

from likes.models import LikeCount, LikeRecord
# Register your models here.

class LikeCountAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'content_object', 'liked_num']

class LikeRecordAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'content_object', 'user', 'like_date']

admin.site.register(LikeCount, LikeCountAdmin)
admin.site.register(LikeRecord, LikeRecordAdmin)
