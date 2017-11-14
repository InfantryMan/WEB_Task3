# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import render_to_string #для render_to_string


from urlparse import urlparse

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class AboutView(TemplateView):
    template_name = "about.html"

def index(request):
    questions = []
    for i in xrange(1, 101):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    #listing(request, "index.html", {'questions': questions,})
    paginator = Paginator(questions, 5)
    page = request.GET.get('page', default=1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'questions': questions})

def hot(request):
    questions = []
    for i in xrange(1, 15):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    #listing(request, "index.html", {'questions': questions,})
    paginator = Paginator(questions, 5)
    page = request.GET.get('page', default=1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'questions': questions})

def tag(request, tag_name):
    questions = []
    for i in xrange(1, 15):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    #listing(request, "index.html", {'questions': questions,})
    paginator = Paginator(questions, 5)
    page = request.GET.get('page', default=1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, "tag.html", {'tag_name': tag_name,
                                        'questions': questions})

def question(request, question_id):
    return render(request, "question.html", {'question_id': question_id})

def ask(request):
    return render(request, "ask.html", {})

def signup(request):
    return render(request, "signup.html", {})

def login(request):
    return render(request, "login.html", {})

def settings(request):
    return render(request, "settings.html", {})

#def listing(request, mytemplate, mymas):
#    question_list = mymas
#    paginator = Paginator(question_list, 5)
#    page = request.GET.get('page', default=1)
#    try:
#        questions = paginator.page(page)
#    except PageNotAnInteger:
#        questions = paginator.page(1)
#    except EmptyPage:
#        questions = paginator.page(paginator.num_pages)
#    return render(request, mytemplate, {'questions': questions})

#def hello(request):
#    return render(request, "_hello.html", {})

#def get_post(request):
#    if request.method=='GET':
#        return render(request, "get_post.html", {
#            'method': request.method,
#            'parameters': request.GET,
#        })
#    else:
#        return render(request, "get_post.html", {
#            'method': request.method,
#            'parametres': request.POST,
#        })