from django.shortcuts import render
from .models import Idea

def index(request):
	idea_list = {'idea_list': list(Idea.objects.order_by('-release_date'))}
	return render(request, 'idealab/index.html', idea_list)
