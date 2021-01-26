from django.db import models

class Chapter(models.Model):
    number = models.CharField(max_length=500, primary_key=True)
    slug = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    content = models.TextField()


class Article(models.Model):
    number = models.CharField(max_length=500, primary_key=True)
    slug = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    content = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
