from django.urls import path

from . import views

urlpatterns = [path('questions', views.questions, name='questions'),
               path('question', views.question, name='question'),
               path('choices', views.choices, name='choices'),
               path('choice', views.choice, name='choice')]
