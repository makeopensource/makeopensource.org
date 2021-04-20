from django.shortcuts import render

def index(request):
	return render(request, 'join/index.html')
