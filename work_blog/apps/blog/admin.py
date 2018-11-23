from django.contrib import admin

from blog.models import BlogType, Blog

# @admin.register(BlogType)---注册方式二
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

# @admin.register(Blog)---注册方式二
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blog_type', 'author', 'get_blog_readnum', 'create_time',  'update_time']

# # @admin.register(ReadNum)---注册方式二
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ['read_num', 'blog']


# 注册方式一：
admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(ReadNum, ReadNumAdmin)