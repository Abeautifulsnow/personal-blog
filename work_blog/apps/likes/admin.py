from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from likes.models import LikeCount, LikeRecord
# Register your models here.

class LikeCountAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'safe_content_object', 'liked_num']

    def safe_content_object(self, obj):
        ct1 = ContentType.objects.get(app_label='blog', model='Blog')
        ct2 = ContentType.objects.get(app_label='comment', model='Comment')
        if obj.content_type == ct1:
            return obj.content_object
        if obj.content_type == ct2:
            return mark_safe(obj.content_object)
    safe_content_object.short_description = '点赞对象'

class LikeRecordAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'safe_content_object', 'user', 'like_date']

    def safe_content_object(self, obj):
        ct1 = ContentType.objects.get(app_label='blog', model='Blog')
        ct2 = ContentType.objects.get(app_label='comment', model='Comment')
        if obj.content_type == ct1:
            return obj.content_object
        if obj.content_type == ct2:
            return mark_safe(obj.content_object)
    safe_content_object.short_description = '点赞对象'


admin.site.register(LikeCount, LikeCountAdmin)
admin.site.register(LikeRecord, LikeRecordAdmin)
