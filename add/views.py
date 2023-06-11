from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def  home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'add/home.html', context)

class PostListView(ListView):
    model = Post # listview
    template_name = 'add/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    model = Post # listview

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post 
    success_url = '/'

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


def about(request):
    return render(request, 'add/about.html', {'title': 'About' })
