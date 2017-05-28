# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_app_shell.urls import urlpatterns as django_app_shell_urls

urlpatterns = [
    url(r'^', include(django_app_shell_urls, namespace='django_app_shell')),
]
