from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.http import HttpResponseRedirect

from blog.models import Blog


class BlogRssFeed(Feed):
    """
    创建一个rss源
    """
    title = '非马梦衢的博客网站'
    link = "/rss/"

    def items(self):
        return Blog.objects.all()
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:blog_detail', args=[item.id,])
        