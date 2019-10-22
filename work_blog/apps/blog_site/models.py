from django.db import models

# Create your models here.


class RelatedLinks(models.Model):
    """
    相关链接表
    """
    link_name = models.CharField(max_length=30, verbose_name='链接名称', null=True, blank=True)
    link_url = models.URLField(verbose_name='链接URL', null=True, blank=True)
    link_desc = models.TextField(verbose_name='链接描述', null=True, blank=True)

    class Meta:
        verbose_name = '相关链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.link_name


class SiteInfo(models.Model):
    """
    关于本站
    """
    site_desc = models.TextField(verbose_name='本站描述', blank=True, null=True)

    class Meta:
        verbose_name = '关于本站'
        verbose_name_plural = verbose_name


class Expectation(models.Model):
    """
    敬请期待
    """
    expect_desc = models.TextField(verbose_name='期待描述', blank=True, null=True)

    class Meta:
        verbose_name = '敬请期待'
        verbose_name_plural = verbose_name
