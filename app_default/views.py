from django.shortcuts import render
from app_projects.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'app_default/home.html', {'projects':projects})
