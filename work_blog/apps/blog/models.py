# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# django-ckeditor富文本编辑器
from ckeditor_uploader.fields import RichTextUploadingField

from read_statistics.models import ReadNumExpandMethod, ReadDetail
# Create your models here.


class BlogType(models.Model):
    """
    博客分类
    """
    type_name = models.CharField(max_length=20, verbose_name='分类名称')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    """
    博文主体
    """
    title = models.CharField(max_length=200, verbose_name='博文')
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name='博客类型')
    # django-ckeditor富文本编辑器
    content = RichTextUploadingField()
    read_detail = GenericRelation(ReadDetail)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time =models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

        ordering = ['-create_time']
    
    def __str__(self):
        return "<Blog: %s>" % self.title
