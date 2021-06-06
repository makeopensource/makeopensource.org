from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Idea, Author
from .forms import IdeaForm

from rest_framework.response import Response
from .serializers import IdeaSerializer, AuthorSerializer
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend


# handles GET and POST requests for /idealab/ideas/
class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'release_date', 'approved']


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# handles GET and POST requests for /idealab/authors/
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# form processing for /idealab/
def index(request):
    if request.method =="POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            authorname = form.cleaned_data['authorname']
            authoremail = form.cleaned_data['authoremail']
            a = Author(name=authorname, email=authoremail)
            a.save()
            b = Idea(title=name, description=desc, author=a)
            b.save()
            return HttpResponseRedirect('/idealab/')
    else:
        form = IdeaForm()

    content_list = {'idea_list': list(Idea.objects.order_by('-release_date')), 'form': form}
    return render(request, 'idealab/index.html', content_list)
