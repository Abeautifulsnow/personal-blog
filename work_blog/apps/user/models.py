# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    用户个人信息
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=20, verbose_name='昵称')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<Profile: %s for %s>' % (self.nick_name, self.user.username)

def get_nickname(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.nick_name
    else:
        return ''

def get_nickname_or_username(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.nick_name
    else:
        return self.username

def has_nickname(self):
    return UserProfile.objects.filter(user=self).exists()

User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname