from pathlib import Path
from django.shortcuts import render

from .models import Chapter, Article


def home(request):
    return render(request, "home.html")


def toc(request):
    return render(request, "toc.html",{
        'chapters': Chapter.objects.all()
    })


def chapter(request, n, slug):
    chapter = Chapter.objects.get(number=n)
    return render(request, "chapter.html", {
        'chapter': chapter
    })


def section(request, n, slug):
    article = Article.objects.get(number=n)
    return render(request, "section.html", {
        'article': article
    })
