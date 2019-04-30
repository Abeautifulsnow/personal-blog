import qrcode
from django.http import HttpResponse
from django.utils import six
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', locals())

def generate_qrcode(request, data):
    # 根据data生成二维码
    img = qrcode.make(data)
    # 使用内存中字节缓冲区的缓冲I / O实现
    buf = six.BytesIO()
    img.save(buf)
    # 返回包含缓冲区完整内容的字节
    image_stream = buf.getvalue()

    return HttpResponse(image_stream, content_type="image/png")