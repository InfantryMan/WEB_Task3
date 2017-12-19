# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime
from django.utils import timezone

class MyUserManager(UserManager):
    def get_top_N(self, N):
        return self.order_by('-likeCount')[0:N]
    def get_top(self):
        return self.order_by('-likeCount')
    def get_by_tag(self, t_name):
        questions = []
        for q in self.all():
            tags_of_question = q.tag.all()
            number_of_tags = tags_of_question.count()
            i = 0
            flag = 0
            while (i < number_of_tags):
                tag = tags_of_question[i].name
                i = i + 1
                if (tag == t_name):
                    flag = 1
            if (flag == 1):
                questions.append(q)
        return questions

class User(AbstractUser):
    rating = models.IntegerField(default = 0, verbose_name=u"Рейтинг")
    objects = MyUserManager()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    avatar = models.ImageField(
        upload_to = 'avatar/%Y/%m/%d',
        default = 'uploads/avatar.jpg',
    )
    def __unicode__(self):
        return "RelateUser: " + self.user.username

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
    objects = MyUserManager()
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    def get_time(self):
        return self.creation_date.strftime( "%Y.%m.%d %H:%M:%S")
    class Meta:
        db_table = 'blogquestions'
        ordering = ['-creation_date']


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"Название тега")
    def __unicode__(self):
        return self.name

class Answer(models.Model):
    question = models.ForeignKey('Question')
    profile = models.ForeignKey('Profile')
    content = models.TextField(verbose_name=u"Текст ответа")
    likeCount = models.IntegerField(default=0)

    def __unicode__(self):
        return "Question: " + self.question.title + "; From: " + self.question.profile.user.username +  " ; Answer From: " + self.profile.user.username

"""
class Answer(models.Model):
    question = models.ForeignKey('Question')
    content = models.TextField(verbose_name=u"Текст ответа")
    likeCount = models.IntegerField(default=0)

class Like(models.Model):
    user = models.OneToOneField(User)
    question = models.OneToOneField(Question, default=0)
    answer = models.OneToOneField(Answer, default=0)



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


