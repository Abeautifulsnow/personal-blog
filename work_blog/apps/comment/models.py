# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Comment(models.Model):
    """
    评论
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='comments', verbose_name='评论用户')

    root = models.ForeignKey('self', null=True, on_delete=models.CASCADE,
                             related_name='root_comment')
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE,
                               related_name='parent_comment')
    reply_to = models.ForeignKey(User, null=True, on_delete=models.CASCADE,
                                 related_name='replies', verbose_name='给()回复')

    class Meta:
        verbose_name = '评论内容'
        verbose_name_plural = verbose_name

        ordering = ['comment_time']

    def __str__(self):
        return self.text
