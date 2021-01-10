from pathlib import Path
from django.shortcuts import render

import markdown
import glob


def home(request):
    return render(request, "home.html")


def toc(request):
    return render(request, "toc.html")


def chapter(request, n, slug):
    base_dir = Path(__file__).resolve().parent.parent
    file_dir = base_dir / 'programme' / f'chapitre-{n}' / 'index.md'
    return render(request, "chapter.html", {
        'content': markdown.Markdown().convert(open(file_dir).read())
    })


def section(request, n, slug):
    base_dir = Path(__file__).resolve().parent.parent

    file_dir = None
    for file in glob.glob(f"{base_dir / 'programme'}/**", recursive=True):
        if f"/{n}.md" in file:
            file_dir = file
            break
    return render(request, "section.html", {
        'content': markdown.Markdown().convert(open(file_dir).read())
    })
