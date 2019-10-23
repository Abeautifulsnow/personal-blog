#!usr/bin/env python
# -*- coding:utf-8 -*-
from django import template
from django.db.models.aggregates import Count

from ..models import Blog, Tag

register = template.Library()


@register.simple_tag
def get_tag_list():
    # 返回标签数量大于0的列表
    return Tag.objects.annotate(total_num=Count("blog")).filter(total_num__gt=0)
