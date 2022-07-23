from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project, Tag, Review

project_list = [
    {
        'id' : '1',
        'title' : 'E-commerce Website',
        'description' : 'Fully Functional E-commerce Website'
    },
    {
        'id' : '2',
        'title' : 'Portfolio Website',
        'description' : 'My Portfolio Website'
    },
    {
        'id' : '3',
        'title' : 'Social Network',
        'description' : 'Best Social Network Ever'
    },
    {
        'id' : '4',
        'title' : 'Travel Guide',
        'description' : 'Find your Destinations Here'
    },
]

def projetcts(request):
    projects = Project.objects.all()
    context = {'projects' : projects }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project' : project_obj}) 
