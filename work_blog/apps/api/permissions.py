"""
对象级别的权限；
希望所有的用户都能看到这些文章，但是也只有创建这些文章的用户才能更新和删除它。
"""
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
    # def has_object_permission(self, request, view, obj):
    #     # 读取权限允许任何请求，
    #     # 所以我们总是允许GET，HEAD或OPTIONS请求。
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
        
    #      # 只有该Blog的所有者才允许写权限。
    #     return obj.author == request.user
