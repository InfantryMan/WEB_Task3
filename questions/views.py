from __future__ import unicode_literals
from django.shortcuts import render
from django.template.loader import render_to_string
from urlparse import urlparse
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http import Http404
from .models import Question, Answer, Tag, Profile, User

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
        object_list = paginator.page(paginator.num_pages)
    return object_list

def index(request):
    try:
        questions = Question.objects.all()
    except questions.DoesNotExist:
        questions = None
    questions = paginate(request, questions)
    return render(request, "index.html", {'questions': questions})

def hot(request):
    questions = Question.objects.get_top()
    questions = paginate(request, questions)
    return render(request, "hot.html", {'questions': questions})

def tag(request, t_name):
    questions = Question.objects.get_by_tag(t_name)
    questions = paginate(request, questions)
    return render(request, "tag.html", {'questions': questions})

def question(request, q_id):
    currentQuestion = Question.objects.get(pk=q_id)
    return render(request, "question.html", {'question': currentQuestion})

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