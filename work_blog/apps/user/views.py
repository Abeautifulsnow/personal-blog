# encoding:utf-8
import string
import random
import time
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.mail import send_mail

from user.forms import LoginForm, RegisterForm, ChangeNicknameForm, BindEmailForm, ChangePwdForm, ForgotPasswordForm
from user.models import UserProfile


def Login_for_modal(request):
    """
    模态框登录页面
    """
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def LoginView(request):
    """
    登录页面
    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return HttpResponseRedirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def Register(request):
    """
    注册
    """
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request=request)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password1']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 清除session
            del request.session['register_code']
            # 登录用户
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(request.GET.get('from', reverse('home')))
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})


def LogoutView(request):
    """
    退出
    """
    logout(request)
    return HttpResponseRedirect(request.GET.get('from', reverse('home')))


def UserInfoView(request):
    """
    用户个人信息
    """
    context = {

    }
    return render(request, 'user_info.html', context)


def ChangeNicknameView(request):
    """
    修改昵称
    """
    redirct_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST, user=request.user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            userprofile, created = UserProfile.objects.get_or_create(user=request.user)
            userprofile.nick_name = nickname_new
            userprofile.save()
            return HttpResponseRedirect(redirct_to)
    else:
        form = ChangeNicknameForm()
    
    context = {
        'page_title': '修改昵称',
        'form_title': '修改昵称',
        'submit_text': '修改',
        'return_back_to': redirct_to,
        'form': form,
    }
    return render(request, 'form.html', context)


def Bind_emailView(request):
    """
    邮箱绑定
    """
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        email_form = BindEmailForm(request.POST, request=request)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            request.user.email = email
            request.user.save()
            # 清除session
            del request.session['bind_email_code']
            return HttpResponseRedirect(redirect_to)
    else:
        email_form = BindEmailForm()
    
    context = {
        'page_title': '绑定邮箱',
        'form_title': '绑定邮箱',
        'submit_text': '绑定',
        'return_back_to': redirect_to,
        'form': email_form,
    }
    return render(request, 'bind_email.html', context)


def send_verification_code(request):
    """
    发送验证码
    """
    email = request.GET.get('email', '')
    send_for = request.GET.get('send_for', '')
    data = {}
    if email != '':
        # 生成验证码
        code = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        now = int(time.time())
        send_code_time = request.session.get('send_code_time', 0)
        if now - send_code_time < 30:
            data['status'] = 'ERROR'
        else:
            request.session[send_for] = code
            request.session['send_code_time'] = now
            # 发送邮件
            send_mail('绑定邮箱', '验证码: %s' % code, '15639936570@189.cn', [email], fail_silently=False)
            data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)


def change_password(request):
    """
    修改密码
    """
    redirect_to = reverse('home')
    if request.method == 'POST':
        form = ChangePwdForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            old_pwd = form.cleaned_data['old_pwd']
            new_pwd1 = form.cleaned_data['new_pwd1']
            user.set_password(new_pwd1)
            user.save()
            logout(request)
            return HttpResponseRedirect(redirect_to)
    else:
        form = ChangePwdForm()
    
    context = {
        'page_title': '修改密码',
        'form_title': '修改密码',
        'submit_text': '修改',
        'return_back_to': redirect_to,
        'form': form,
    }
    return render(request, 'form.html', context)

def forgot_pwd(request):
    """
    忘记密码
    """
    redirect_to = reverse('user:login')
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_pwd1 = form.cleaned_data['new_pwd1']
            user = User.objects.get(email=email)
            user.set_password(new_pwd1)
            user.save()
            # 清除session
            del request.session['forgot_password_code']
            return HttpResponseRedirect(redirect_to)
    else:
        form = ForgotPasswordForm()
    
    context = {
        'page_title': '重置密码',
        'form_title': '重置密码',
        'submit_text': '重置',
        'return_back_to': redirect_to,
        'form': form,
    }
    return render(request, 'forgot_pwd.html', context)
