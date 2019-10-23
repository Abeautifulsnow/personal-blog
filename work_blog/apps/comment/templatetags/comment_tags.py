#!usr/bin/env python
# -*- coding:utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import Comment
from ..forms import CommentForm

register = template.Library()


@register.simple_tag
def get_comment_count(obj):
    # 获取评论数量,并向前端发送
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()


@register.simple_tag
def get_comment_form(obj):
    # 获取blog的content_type
    content_type = ContentType.objects.get_for_model(obj)
    # 评论表单,Form动态初始化initial。
    data = {}
    data["content_type"] = content_type.model
    data["object_id"] = obj.pk
    data["reply_comment_id"] = 0
    form = CommentForm(initial=data)
    return form


@register.simple_tag
def get_comment_list(obj):
    # 获取blog的content_type
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(
        content_type=content_type, object_id=obj.pk, parent=None
    )
    return comments.order_by("-comment_time")
