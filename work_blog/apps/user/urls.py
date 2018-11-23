# -*- coding:utf-8 -*-
from django.urls import path

from user.views import LoginView, Register, Login_for_modal, LogoutView, UserInfoView, ChangeNicknameView, \
                        Bind_emailView, send_verification_code, change_password, forgot_pwd

urlpatterns = [
    # 模态框登录界面
    path('login_for_modal/', Login_for_modal, name='login_for_modal'),
    # 登录界面
    path('login/', LoginView, name="login"),
    # 用户退出
    path("logout/", LogoutView, name="logout"),
    # 用户注册
    path('register/', Register, name='register'),
    # 用户个人信息
    path("user_info/", UserInfoView, name="user_info"),
    # 用户昵称修改
    path("change_nickname/", ChangeNicknameView, name="change_nickname"),
    # 用户邮箱绑定
    path("bind_email/", Bind_emailView, name="bind_email"),
    # 验证码链接
    path('bind_email_code/', send_verification_code, name='bind_email_code'),
    # 修改密码
    path('change_password/', change_password, name='change_password'),
    # 忘记密码
    path('forgot_password/', forgot_pwd, name='forgot_password')
]

app_name = 'user'