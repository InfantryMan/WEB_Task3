# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from questions.models import *

# Register your models here.

class AdminModel(admin.ModelAdmin):
    pass
admin.site.register(Question, AdminModel)
admin.site.register(Answer, AdminModel)
admin.site.register(User, AdminModel)
admin.site.register(Profile, AdminModel)
admin.site.register(Tag, AdminModel)
