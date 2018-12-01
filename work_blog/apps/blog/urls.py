# encoding: utf-8
from django.urls import path
from blog.views import blog_detail, blogs_type, blog_list, blogs_by_date, blog_edit, add_ajax, add

urlpatterns = [
    path("", blog_list, name="blog_list"),
    # http://127.0.0.1:8000/blog/1 博客详情页
    path('<int:blog_pk>/', blog_detail, name='blog_detail'),
    # 增加博客页面
    path('blog_add', add, name='blog_add'),
    path("blog_add_ajax", add_ajax, name="add_ajax"),
    # 博客编辑
    path('edit/<int:blog_pk>/', blog_edit, name="blog_edit"),
    # 博客分类页面
    path("type/<int:blog_type_pk>/", blogs_type, name="blogs_type"),
    # 按日期分类
    path("date/<int:year>/<int:month>", blogs_by_date, name="blogs_by_date")
]

app_name = 'blog'
