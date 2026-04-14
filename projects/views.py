from django.shortcuts import render
from .models import Project


def projects_view(request):
    featured = Project.objects.filter(is_featured=True).order_by('-year')[:3]
    all_projects = Project.objects.all().order_by('-year')
    context = {
        'featured_projects': featured,
        'projects': all_projects,
    }
    return render(request, 'projects/project.html', context)