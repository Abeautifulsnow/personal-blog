from django_hosts import patterns, host
from django.conf import settings


host_patterns = patterns('',
    host(r'www', settings.DEFAULT_HOST, name='www'),
    host(r'tools.runstone.top', 'erweima.urls', name='tools'),
)