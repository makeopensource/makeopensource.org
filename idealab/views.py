from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Idea, Author

from .forms import IdeaForm

def index(request):
    if request.method =="POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            authorname = form.cleaned_data['authorname']
            authoremail = form.cleaned_data['authoremail']
            authorgithub = form.cleaned_data['authorgithub']
            a = Author(name=authorname, email=authoremail, github=authorgithub)
            a.save()
            b = Idea(title=name, description=desc, author=a)
            b.save()
            return HttpResponseRedirect('/idealab/')
    else:
        form = IdeaForm()

    content_list = {'idea_list': list(Idea.objects.order_by('-release_date')), 'form': form}
    return render(request, 'idealab/index.html', content_list)
