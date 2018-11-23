# encoding:utf-8
from django.urls import path

from likes.views import like_change

urlpatterns = [
    path('like_change', like_change, name="like_change")
] 
app_name = 'likes'