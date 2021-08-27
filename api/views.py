from django.shortcuts import render

def page_not_found(request, exception):
    return render(request, 'api/page_not_found.html')

def error(request):
    return render(request, 'api/page_not_found.html')