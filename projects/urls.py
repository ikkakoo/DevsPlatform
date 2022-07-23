from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from projects.views import projetcts, project


urlpatterns = [
    path('', projetcts, name='projects'),
    path('project/<str:pk>/', project, name='project')
]