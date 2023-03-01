from django.shortcuts import render
from .models import Post 

from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  
    ordering = ['-date_posted'] #organice the posts by date published

class PostDetailView(DetailView):
    model = Post
   

def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog_app/index.html', context)

def about(request):

    return render(request, 'blog_app/about.html')