#!usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum

from blog.models import Blog
from read_statistics.models import ReadNum, ReadDetail

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(Blog)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        # if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
        #     # 存在记录
        #     readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        # else:
        #     # 不存在记录
        #     readnum = ReadNum(content_type=ct, object_id=obj.pk)
        """上面注释部分可简写为下面部分，利用get_or_create函数(属于querysets),总阅读数+1"""
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
        # 判断记录是否存在
        # if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date):
        #     read_detail = ReadDetail.objects.get(content_type=ct, object_id=obj.pk, date=date)
        # else:
        #     read_detail = ReadDetail(content_type=ct, object_id=obj.pk, date=date)
        """当天阅读数+1"""
        # 取出现在时间
        date = timezone.now().date()
        read_detail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        read_detail.read_num += 1
        read_detail.save()

    return key

def get_seven_days_ReadData(content_type):
    """
    获取过去7天每天访问量
    """
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0 , -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        # 聚合函数Sum,aggreate返回的是一个dictionary（字典）类型的值{'read_num_sum': Sum()}
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums

def get_today_HotData(content_type):
    """
    今日热门阅读
    """
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details[:9]

def get_yesterday_HotData(content_type):
    """
    昨日热门阅读
    """
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_num')
    return read_details[:9]
