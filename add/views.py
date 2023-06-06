from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


def  home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'add/home.html', context)

class PostListView(ListView):
    model = Post # listview
    template_name = 'add/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    model = Post # listview

def about(request):
    return render(request, 'add/about.html', {'title': 'About' })