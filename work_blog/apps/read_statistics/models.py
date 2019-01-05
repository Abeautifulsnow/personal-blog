# encoding:utf-8
from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.


class ReadNumExpandMethod(object):
    # 获取阅读量
    def get_blog_readnum(self):
        try:
            # 获取content类型
            ct = ContentType.objects.get_for_model(self)
            # 获取readnum
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    get_blog_readnum.short_description = '阅读数量统计'


class ReadNum(models.Model):
    """
    阅读统计
    """
    read_num = models.IntegerField(default=0, verbose_name='阅读数')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '阅读统计'
        verbose_name_plural = verbose_name


class ReadDetail(models.Model):
    """
    阅读详情
    """
    date = models.DateField(default=timezone.now, verbose_name='日期')
    read_num = models.IntegerField(default=0, verbose_name='阅读数')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '阅读详情'
        verbose_name_plural = verbose_name