from django.contrib import admin

from blog.models import BlogType, Blog

# @admin.register(BlogType)---注册方式二
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

# @admin.register(Blog)---注册方式二
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blog_type', 'author', 'get_blog_readnum', 'create_time',  'update_time']
    list_display_links = ['title']
    date_hierarchy = 'create_time'
    list_filter = ['blog_type', 'author']
    list_per_page = 50
# # @admin.register(ReadNum)---注册方式二
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ['read_num', 'blog']

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(BlogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    # def show_content(self, obj):
    #     return obj.content[:30]
    # show_content.short_description = '博客内容'


# 注册方式一：
admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(ReadNum, ReadNumAdmin)
admin.site.site_header = '博客网站管理'
admin.site.site_title = '博客后台管理'