"""ask_rmigranov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from questions import views

from django.contrib import admin

urlpatterns = [

    url(r'^hot/$', views.index, name = 'hot'),
    url(r'^tag/(?P<tag_name>\w+)/$', views.tag, name = 'tag'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name = 'question'),

    url(r'^signup/$', views.signup, name = 'signup'),
#    url(r'^hello/', views.hello),
    url(r'^ask/$', views.ask, name = 'ask'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^settings/$', views.settings, name = 'settings'),
    url(r'^', views.index, name = 'index'),
]