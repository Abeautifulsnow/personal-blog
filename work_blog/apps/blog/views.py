# coding:utf-8
import json
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import *
from work_blog.settings.base import EACH_PAGE_BLOGS_NUM
from read_statistics.utils import read_statistics_once_read
# from .forms import BlogForm
from user.models import UserProfile
# Create your views here.

# 装饰器，管理员判断
def check_amdin(func):
    def wrapper(request):
        if request.user.is_authenticated():
            if request.user.is_superuser:
                return func(request)
        context = {
            'redirect_to': '/',
            'goto_time': 3000,
            'goto_page': True,
            'msg': '您不是管理员，不能进入这个界面'
        }
        return render(request, 'error.html', context)

    return wrapper


def get_blog_list_common(request, all_blogs):
    """
    共同代码模板
    """
    blog_types = BlogType.objects.all()
    tags = Tag.objects.all()
    blog_dates = Blog.objects.dates('create_time', 'month', order='DESC')
    # 博客分页
    p = Paginator(all_blogs, EACH_PAGE_BLOGS_NUM)   # 每each_page_blogs_num篇分一页
    page_num = request.GET.get('page', 1)   # 获取URL的页码参数（GET请求）
    # 获取当前页码下的博客
    page_of_blogs = p.get_page(page_num)
    # 获取当前页码
    current_page_num = page_of_blogs.number
    # 获取当前页码的前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                list(range(current_page_num, min(current_page_num + 2, p.num_pages) + 1))
    # 加上省略页码标记...
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if p.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != p.num_pages:
        page_range.append(p.num_pages)

    """
        # 获取博客分类的对应博客数量(方案一)
        blog_types = BlogType.objects.all()
        blog_types_list = [] # 将blog_type_list返回给字典context['blog_types']
        for blog_type in blog_types:
            blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
            blog_types_list.append(blog_type)
        
        # 获取博客分类的对应博客数量(方案二)
        blog_types = BlogType.objects.all()
        for blog_type in blog_types:
            blog_type.blog_count = blog_type.blog_set.count  # blog_type是Blog的外键，可以采用blog_set的方式

        # 获取博客分类的对应博客数量(方案三)
        # 参考链接：https://docs.djangoproject.com/zh-hans/2.1/ref/models/querysets/#annotate
        blog_types = BlogType.objects.annotate(blog_count=Count('blog')) # 直接返回给字典（需要额外导入Count方法）
    """

    # 获取日期归档的博客分类数量（方案一：字典方式;方案二：annotate方式，略麻烦）
    blog_dates = Blog.objects.dates('create_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(create_time__year=blog_date.year, 
                                        create_time__month=blog_date.month ).count()
        blog_dates_dict[blog_date] = blog_count

    context = {
        'page_of_blogs': page_of_blogs,
        'tags': tags,
        'blog_types': blog_types,
        'page_range': page_range,
        'blog_dates': blog_dates_dict,
    }
    return context


def blog_list(request):
    """
    博客列表页
    """
    all_blogs = Blog.objects.all()

    # 搜索功能
    search_keywords = request.GET.get('keywords', '')
    if search_keywords:
        all_blogs = all_blogs.filter(Q(title__icontains=search_keywords)|Q(content__icontains=search_keywords))

    # 调用get_blog_list_common函数中的context
    context = get_blog_list_common(request, all_blogs)
    return render(request, 'blog_list.html', context)


def blogs_type(request, blog_type_pk):
    """
    博客类别分类
    """
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    all_blogs = Blog.objects.filter(blog_type=blog_type)

    # 调用get_blog_list_common函数中的context
    context = get_blog_list_common(request, all_blogs)
    # 在context字典中新增加key为'blog_type'的字典
    context['blog_type'] = blog_type
    return render(request, 'blogs_type.html', context)


def blogs_by_date(request, year, month):
    """
    博客按日期分类
    """
    all_blogs = Blog.objects.filter(create_time__year=year, create_time__month=month)
    blog_by_date = '%s年%s月' % (year, month)

    # 调用get_blog_list_common函数中的context
    context = get_blog_list_common(request, all_blogs)
    # 在context字典中新增加key为'blog_by_date'的字典
    context['blog_by_date'] = blog_by_date
    return render(request, 'blogs_by_date.html', context)


def blogs_tags(request, tag_pk):
    """
    博客标签云
    """
    tag = get_object_or_404(Tag, pk=tag_pk)
    all_blogs = Blog.objects.filter(tag=tag)

    context = get_blog_list_common(request, all_blogs)
    context['tag'] = tag
    return render(request, 'blogs_tags.html', context)


def blog_detail(request, blog_pk):
    """
    博客详情页
    """
    blog = get_object_or_404(Blog, pk=blog_pk)
    # 调用read_statistics.utils中的read_statistics_once_read函数
    read_cookie_key = read_statistics_once_read(request, blog)

    # 博客下一页
    next_blog = Blog.objects.filter(create_time__gt=blog.create_time).last()
    # 博客上一页
    pre_blog = Blog.objects.filter(create_time__lt=blog.create_time).first()

    context = {
        'blog': blog,
        'pre_blog': pre_blog,
        'next_blog': next_blog,
    }
    response = render(request, 'blog_detail.html', context)  # 响应
    # step1：给浏览器设置cookie，用于判断
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记
    return response

@login_required
def blog_edit(request, blog_pk):
    """
    博客内容编辑
    """
    blog = Blog.objects.get(id=blog_pk)
    
    if request.user != blog.author:
        raise Http404
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog.title = title
        blog.content = content
        blog.save()
        return HttpResponseRedirect(reverse('blog:blog_list'))
    else:
        pass
    context = {
        'blog': blog,
    }
    return render(request, 'blog_edit.html', context)

@check_amdin
def add(request):
    blog_types = BlogType.objects.all()
    data = {
        'blog_types': blog_types,
    }
    return render(request, 'add_blog.html', data, context_instance=RequestContext(request))

@check_amdin
def add_ajax(request):
    data = {}
    try:
        if request.method != 'POST':
            raise Exception('methos error')
        #获取数据
        #这些相关数据都是前端页面表单中的字段
        #且和我博客模型一一对应，你根据实际情况修改即可
        blog_title = request.POST.get('title')
        blog_types = request.POST.getlist('blog_type')
        blog_content = request.POST.get('content')

        #处理blog_types
        blog_type_ids = []
        for blog_type in blog_types:
            try:
                blog_type_id = int(blog_type)
                blog_type_ids.append(blog_type_id)
            except:
                pass
        if len(blog_title) <= 0 or len(blog_title) >= 50:
            raise Exception('请输入一个不超过50个字符的标题')
        if len(blog_type_ids) < 1:
            raise Exception('请选择"推荐"之外的至少一个类别')
        if len(blog_content) == 0:
            raise Exception('尚未写入任何博文')
        
        #新增博文
        blog = Blog()
        blog.title = blog_title #标题
        
        #这里后面我还要修改，统一用Django的用户系统
        #Author是一个作者模型
        blog.author = UserProfile.objects.all()[0].username
        
        blog.content = blog_content #博客内容
        blog.save()
 
        #处理多对多，需要博文保存后才能处理，且新增后无需使用save方法
        for blog_type in BlogType.objects.filter(id__in = blog_type_ids):
            blog.blog_type.add(blog_type)        
 
        #返回结果
        data['success'] = True
        data['message'] = reverse('blog:blog_detail', args = [blog.id,])
    except Exception as e:
        data['success'] = False
        data['message'] = e.message
    
    return HttpResponse(json.dumps(data), content_type = 'application/json')
