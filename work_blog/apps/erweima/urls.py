from django.urls import path, re_path
from .views import index, generate_qrcode


urlpatterns = [
    path('erweima/index', index, name='qrcode_home'),
    re_path('^erweima/qrcode/(.+)$', generate_qrcode, name='qrcode_img'),
]
