from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def toc(request):
    return render(request, "toc.html")
