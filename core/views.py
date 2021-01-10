from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def toc(request):
    return render(request, "toc.html")


def chapter(request, n, slug):
    return render(request, "chapter.html")


def section(request, n, slug):
    return render(request, "section.html")
