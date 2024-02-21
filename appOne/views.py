from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

#!HOME page
def home(request):
    context = {
        
    }
    return render(request, 'appOne\home.html', context)





#! PROJECTS page
def projects(request):
    project = Project.objects.all()
    context = {
        'projects':project
    }
    return render(request, 'appOne\projects.html', context)


def viewProject(request, pk):
    project = Project.objects.get(id = pk)

    context = {
        'project':project,
    }
    return render(request, 'appOne/viewProject.html', context)


#! Route To add project
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'appOne/projectForm.html', context)


#! Route to update project
def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, 'appOne/projectForm.html', context)


#! Route to delete existing project
def deleteProject(request, pk):
    project = Project.objects.get(id = pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'project':project
    }
    return render(request, 'appOne/deleteProject.html', context)




    
#! ABOUT page
def about(request):
    context = {
        
    }
    return render(request, 'appOne/about.html', context)


#! CONTACT page
def contact(request):
    context = {
        
    }
    return render(request, 'appOne\contact.html', context)