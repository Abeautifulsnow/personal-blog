from django.shortcuts import render

# Create your views here.


def list_link_site_expect(obj):
    """
    展示links、about_site、expectation
    :param obj: model对象
    :return:
    """
    result = obj.objects.all()
    return result
