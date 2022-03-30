#!usr/bin/env python
# -*- coding:utf-8 -*-
from .models import *


def change_info(request):
    """

    :param request:
    :return:
    """
    # 每一次访问，网站总访问次数加一
    try:
        count_nums = VisitNum.objects.all()[0]
        count_nums.all_count += 1
        count_nums.save()

        # 记录访问ip和每个ip的次数
        if 'HTTP_X_FORWARDED_FOR' in request.META:      # 获取ip
            client_ip = request.META['HTTP_X_FORWARDED_FOR']
            client_ip = client_ip.split(",")[0]      # 这里是真实的ip
        else:
            client_ip = request.META['REMOTE_ADDR']     # 这里获得代理ip
        print(client_ip)

        ip_exist = UserIP.objects.filter(ip=str(client_ip))
        if ip_exist:
            uobj = ip_exist[0]
            uobj.visit_count += 1
        else:
            uobj = UserIP()
            uobj.ip = client_ip
            uobj.visit_count += 1
        uobj.save()
    except Exception as e:
        pass
