from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('sommaire/', views.toc),
]
