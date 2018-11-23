#!usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path

from comment.views import update_comment

urlpatterns = [
    path('update_comment', update_comment, name='upadte_comment'),
]

app_name = 'comment'
