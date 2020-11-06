from django.shortcuts import render
from .models import Projects

# Create your views here.


def projectsTemplate(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/projectsTemplate.html', {'projects': projects})
