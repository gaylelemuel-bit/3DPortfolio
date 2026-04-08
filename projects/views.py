from django.shortcuts import render
from .models import Project 

# Create your views here.
def projects_view(request):
    project_list = Project.objects.all().order_by('-year')
    context = {
        'projects': project_list,
    }
    return render(request, 'projects/project.html', context)