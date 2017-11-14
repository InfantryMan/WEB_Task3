# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    create_date = models.DateTimeField(verbose_name=u"Время создания вопроса")

    like = models.OneToOneField('Like')
    profile = models.ForeignKey('Profile')
    tag = models.ManyToManyField('Tag')

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Profile(models.Model):
    avatar = models.CharField(max_length=120)

class Answer(models.Model):
    question = models.ForeignKey('Question')
    like = models.OneToOneField('Like')

class Tag(models.Model):

class Like(models.Model):
