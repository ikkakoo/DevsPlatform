from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from projects.views import projetcts, project, create_project


urlpatterns = [
    path('', projetcts, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', create_project, name='create-project')
]