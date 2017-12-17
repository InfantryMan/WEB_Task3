# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import render_to_string #для render_to_string

from urlparse import urlparse

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import Http404

class AboutView(TemplateView):
    template_name = "about.html"

def vote(request):
    try:
      qid = int(request.POST.get('qid'))
    except:
        return JsonResponse(dict(error='bad question id'))
    vote = request.POST.get('vote')
    return JsonResponse({'test':1})


"""
def profile(request):
    profile = request.user.profile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
            profile = form.save()

"""
def paginate(request, object_list):
    try:
        size = int(request.GET.get('size', default = 10))
    except ValueError:
        size = 10
    if size > 100:
        size = 10
    try:
        page = int(request.GET.get('page', default = 1 ))
    except ValueError:
        raise Http404
    paginator = Paginator(object_list, size)
    try:
        object_list = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return object_list

"""
def paginate1(object_list, page, size):
    paginator = Paginator(object_list, size)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list
"""

def index(request):
    questions = []
    for i in xrange(1, 101):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    page = request.GET.get('page', default=1)
    questions = paginate(request, questions)
    return render(request, "index.html", {'questions': questions})

"""
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
"""

def hot(request):
    questions = []
    for i in xrange(1, 15):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    page = request.GET.get('page', default=1)
    questions = paginate(request, questions)
    return render(request, "hot.html", {'questions': questions})

def tag(request, t_name):
    questions = []
    for i in xrange(1, 15):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    page = request.GET.get('page', default=1)
    questions = paginate(request, questions)
    return render(request, "tag.html", {'tag_name': t_name,
                                        'questions': questions})

def question(request, q_id):
    return render(request, "question.html", {'q_id': q_id})

def profile(request):
    return render(request, 'profile.html', {})

def ask(request):
    return render(request, "ask.html", {})

def signup(request):
    return render(request, "signup.html", {})

def login(request):
    return render(request, "login.html", {})

def settings(request):
    return render(request, "settings.html", {})

def static(request):
    return render(request, "example.html", {})

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

def get_post(request):
    if request.method=='GET':
        return render(request, "get_post.html", {
            'method': request.method,
            'parameters': request.GET,
        })
    else:
        return render(request, "get_post.html", {
            'method': request.method,
            'parametres': request.POST,
        })