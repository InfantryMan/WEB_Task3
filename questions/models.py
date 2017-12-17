# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime

class User(AbstractUser):
    upload = models.ImageField(default='static/img/avatar.jpg', upload_to='uploads/%Y/%m/%d')
    rating = models.IntegerField(default = 0, verbose_name=u"Рейтинг")
    #objects = MyUserManager()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    avatar = models.ImageField(
        upload_to = 'avatar/%Y/%m/%d',
        default = 'uploads/avatar.jpg',
    )
"""
class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    content = models.TextField(verbose_name=u"Полное описание вопроса")
    creation_date = models.DateTimeField(verbose_name=u"Время создания вопроса", blank = True)

    likeCount = models.IntegerField(default = 0)
    profile = models.ForeignKey('Profile')
    tag = models.ManyToManyField('Tag')

    is_active = models.BooleanField(default=True,
                                    verbose_name=u"Доступность вопроса",
                                    )
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/post1/%d/' % self.pk
    class Meta:
        db_table = 'blogquestions'
        ordering = ['-creation_date']

class Answer(models.Model):
    question = models.ForeignKey('Question')
    content = models.TextField(verbose_name=u"Текст ответа")
    likeCount = models.IntegerField(default=0)

class Like(models.Model):
    user = models.OneToOneField(User)
    question = models.OneToOneField(Question, default=0)
    answer = models.OneToOneField(Answer, default=0)

class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"Название тега")

"""


"""
class MyUserManager(UserManager):
    def get_top_N(self, N):
        return self.order_by('-rating')[0:N]

class User(AbstractUser):
    upload = models.ImageField(default='static/img/avatar.jpg', upload_to='uploads/%Y/%m/%d')
    rating = models.IntegerField(default = 0, verbose_name=u"Рейтинг")
    objects = MyUserManager()
"""

"""
class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(
        upload_to = 'avatar/%Y/%m/%d',
        default = 'uploads/avatar.jpg')
"""

"""
class Answer(models.Model):
    question = models.ForeignKey('Question')
    like = models.OneToOneField('Like')
"""

