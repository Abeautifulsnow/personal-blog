from django.urls import path, re_path
from .views import index, generate_qrcode


urlpatterns = [
    path('index', index, name='qrcode_home'),
    re_path('^qrcode/(.+)$', generate_qrcode, name='qrcode_img'),
]

app_name = 'erweima'