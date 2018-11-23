# encoding:utf-8
import datetime
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache

from blog.models import Blog
from read_statistics.utils import get_seven_days_ReadData, get_today_HotData, get_yesterday_HotData


def get_seven_day_HotBlogs():
    """
    7天热门阅读
    """
    today = timezone.now().date()
    last_seven_date = today - datetime.timedelta(days=7)
    blogs = Blog.objects\
        .filter(read_detail__date__lt=today, read_detail__date__gte=last_seven_date)\
        .values('id', 'title')\
        .annotate(read_num_sum=Sum('read_detail__read_num'))\
        .order_by('-read_num_sum')
    return blogs[:9]


def HomeView(request):
    """
    首页
    """
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_ReadData(blog_content_type)
    today_HotData = get_today_HotData(blog_content_type)
    yesterday_HotData = get_yesterday_HotData(blog_content_type)

    # 获取7天热门博客的缓存数据
    seven_day_HotBlog = cache.get('seven_day_HotBlog')
    if seven_day_HotBlog is None:
        seven_day_HotBlog = get_seven_day_HotBlogs()
        cache.set('seven_day_HotBlog', seven_day_HotBlog, 3600)
    # 测试
        print('calc')
    else:
        print('Use cache ')

    context = {
        'dates': dates,
        'read_nums': read_nums,
        'today_HotData': today_HotData,
        'yesterday_HotData': yesterday_HotData,
        'seven_day_HotBlog': seven_day_HotBlog,
    }
    return render(request, 'home.html', context)
