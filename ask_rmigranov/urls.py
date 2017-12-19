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
    url(r'^profile/?',                  views.profile),
    url(r'^hot/$',                      views.hot, name = 'hot'),
    url(r'^tag/(?P<t_name>\w+\W*)/$',      views.tag, name = 'tag'),
    url(r'^question/(?P<q_id>[0-9]+)/$', views.question, name = 'question'),
    url(r'^signup/$',                   views.signup, name = 'signup'),
    url(r'^ask/$',                      views.ask, name = 'ask'),
    url(r'^login/$',                    views.login, name = 'login'),
    url(r'^settings/$',                 views.settings, name = 'settings'),
    url(r'^admin/',                     admin.site.urls),
    url(r'^get_post/',                  views.get_post),
    url(r'^static/',                    views.static),
    url(r'^',                           views.index, name = 'index'),
]