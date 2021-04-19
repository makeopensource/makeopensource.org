from django.shortcuts import render
from .models import Project

def index(request):
	projects = {'projects': list(Project.objects.order_by('-release_date'))}
	return render(request, 'projects/index.html', projects)
