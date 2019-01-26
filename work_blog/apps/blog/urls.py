# encoding: utf-8
from django.urls import path, re_path
from blog.views import blog_detail, blogs_type, blogs_tags, blog_list, blogs_by_date, all_types

urlpatterns = [
    path("", blog_list, name="blog_list"),
    # http://127.0.0.1:8000/blog/1 博客详情页
    path('<int:blog_pk>/', blog_detail, name='blog_detail'),
    # 博客分类页面
    path('type/<int:blog_type_pk>/', blogs_type, name="blogs_type"),
    # 博客标签页面
    re_path(r'^tag/(?P<tag_pk>\d+)/$', blogs_tags, name='blogs_tags'),
    # 按日期分类
    path('date/<int:year>/<int:month>', blogs_by_date, name="blogs_by_date"),
    # 所有分类归纳页
    path('all_types/', all_types, name="all_types"),
]

app_name = 'blog'
