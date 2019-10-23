# encoding:utf-8
import datetime
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache

from blog.models import Blog, BlogType
from blog.utils import change_info
from read_statistics.utils import get_seven_days_ReadData, get_today_HotData, get_yesterday_HotData
from read_statistics.models import ReadNum
from blog_site.views import list_link_site_expect
from blog_site.models import SiteInfo, Expectation


def get_seven_day_hotblogs():
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
    blog_nums = Blog.objects.all().count()
    blog_types = BlogType.objects.all()[:15]
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_ReadData(blog_content_type)
    today_HotData = get_today_HotData(blog_content_type)
    yesterday_HotData = get_yesterday_HotData(blog_content_type)
    new_blogs = Blog.objects.all().order_by('-create_time')[:12]
    # 获取关于站点信息
    about_site = list_link_site_expect(SiteInfo).first()
    # 敬请期待
    expectation = list_link_site_expect(Expectation).first()

    # 获取所有博客阅读量并排序
    blog_dict = {}
    nums = ReadNum.objects.all().order_by('-read_num')[:12]
    for num in nums:
        blog = Blog.objects.get(pk=num.object_id)
        blog_all_readnum = num.read_num
        blog_dict[blog] = blog_all_readnum
    
    # 获取7天热门博客的缓存数据
    seven_day_HotBlog = cache.get('seven_day_HotBlog')
    if seven_day_HotBlog is None:
        seven_day_HotBlog = get_seven_day_hotblogs()
        cache.set('seven_day_HotBlog', seven_day_HotBlog, 3600)
        # 测试
        print('calc')
    else:
        print('Use cache ')

    change_info(request)
    context = {
        'blog_nums': blog_nums,
        'blog_types': blog_types,
        'dates': dates,
        'read_nums': read_nums,
        'today_HotData': today_HotData,
        'yesterday_HotData': yesterday_HotData,
        'seven_day_HotBlog': seven_day_HotBlog,
        'new_blogs': new_blogs,
        'blog_dict': blog_dict,
        'about_site': about_site,
        'expectation': expectation,
    }
    return render(request, 'home.html', context)
