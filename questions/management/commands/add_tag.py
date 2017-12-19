from django.core.management.base import BaseCommand, CommandError
from questions.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        tag_name = ["C++", "Java", "Python", "Django", "Gunicorn", "C", "OOP", "JavaScript", "PHP", "HTML", "CSS", "MySQL"]
        i = 0
        while i < len(tag_name):
            tag = Tag(name=tag_name[i])
            tag.save()
            i = i + 1

