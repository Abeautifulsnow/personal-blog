from django.contrib import admin

from blog.models import BlogType, Tag, Blog, UserIP, VisitNum

# @admin.register(BlogType)---注册方式二
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']
    list_display_links = ['type_name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 30


# @admin.register(Blog)---注册方式二
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blog_type', 'author', 'create_time',  'update_time', 'show_tag', 'get_blog_readnum']
    list_display_links = ['title']
    date_hierarchy = 'create_time'
    list_filter = ['blog_type', 'author']
    list_per_page = 50
    filter_horizontal = ('tag',)

    def show_tag(self, obj):
        print(type(obj))
        return [i.name for i in obj.tag.all()]
    show_tag.short_description = '博客标签'

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

class UserIPAdmin(admin.ModelAdmin):
    list_display = ['ip', 'visit_count']
    list_per_page = 30
    list_filter = ['ip']


class VisitNumAdmin(admin.ModelAdmin):
    list_display = ['all_count']


# 注册方式一：
admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(UserIP, UserIPAdmin)
admin.site.register(VisitNum, VisitNumAdmin)
# admin.site.register(ReadNum, ReadNumAdmin)
admin.site.site_header = '博客网站管理'
admin.site.site_title = '博客后台管理'