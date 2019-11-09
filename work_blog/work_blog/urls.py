"""work_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers

from work_blog.views import HomeView
from work_blog.settings.base import MEDIA_URL, MEDIA_ROOT
from api import views as apiview

router = routers.DefaultRouter()
router.register(r'users', apiview.UserListSet)
router.register(r'blogtypes', apiview.BlogTypeListSet)
router.register(r'tags', apiview.TagListSet)
router.register(r'blogs', apiview.BlogListSet)


urlpatterns = [
    # 主页
    path("", HomeView, name="home"),
    path("admin/", admin.site.urls),
    path("login/github/", include("social_django.urls", namespace="social")),
    path("ckeditor", include("ckeditor_uploader.urls")),
    # app url register
    path("blog/", include("blog.urls", namespace="blog")),
    path("comment/", include("comment.urls", namespace="comment")),
    path("likes/", include("likes.urls", namespace="likes")),
    path("user/", include("user.urls", namespace="user")),
    # rest api register enter
    path("api/v1/", include(router.urls)),
    path("api_auth/", include("rest_framework.urls", namespace="rest_framework")),
    # haystack
    path('search/', include('haystack.urls')),
    # 二维码
    # path('erweima/', include('erweima.urls', namespace='erweima')),
    # 图片文件上传途径
    # re_path(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT})
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)