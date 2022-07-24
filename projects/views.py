from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Project, Tag, Review
from projects.forms import ProjectForm

def projetcts(request):
    projects = Project.objects.all()
    context = {'projects' : projects }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project' : project_obj}) 

def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)



