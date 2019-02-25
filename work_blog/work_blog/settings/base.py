# encoding:utf-8
"""
Django settings for work_blog project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 定义总文件夹路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))



# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
    # 我的应用
    'blog',
    # 阅读统计
    'read_statistics',
    # 博客评论
    'comment',
    # 点赞app
    'likes',
    # 用户user
    'user',
]

MIDDLEWARE = [
    # 全局cache
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     # 全局cache
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'work_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 在user的context_processors.py文件中自定义login_modal_form,然后自动在模板中引用
                'user.context_processors.login_modal_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'work_blog.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# 配置静态文件路径
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# MEDIA配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"

# 自定义CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat', '-', 'Maximize',
                     'ShowBlocks', '-', "CodeSnippet", 'Subscript', 'Superscript'],
                    ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                     'HiddenField'],
                    ['Bold', 'Italic', 'Underline', 'Strike', '-'],
                    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ['Link', 'Unlink', 'Anchor'],
                    ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
                    ['Styles', 'Format', 'Font', 'FontSize'],
                    ['TextColor', 'BGColor'],

                    ),

        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils',]),
        'width': 'auto',
        'tabSpaces': 4,
        'toolbarCanCollapse': True,
        'codeSnippet_theme': 'railscasts',
    },
    'comment_ckeditor': {
        'toolbar': 'Custom',
        'toolbar_Custom': (
                            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
                            ['NumberedList', 'BulletedList'],
                            ['Link', 'Unlink'],
                            ['RemoveFormat', 'TextColor', 'BGColor'],
                            ['Smiley', 'SpecialChar', 'Blockquote'],
                            ["CodeSnippet"],
                        ),
        'extraPlugins': 'codesnippet',

        'width': 'auto',
        'height': 180,
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# 自定义分页参数
EACH_PAGE_BLOGS_NUM = 8

# # 缓存设置
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }

# redis缓存
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': os.environ['redis_passwd'],
        },
    },
}
REDIS_TIMEOUT = 7*24*60*60
CUBES_REDIS_TIMEOUT = 60*60
NEVER_REDIS_TIMEOUT = 365*24*60*60

# rest_framework设置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}