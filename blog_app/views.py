from django.shortcuts import render
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  
    ordering = ['-date_posted'] #organice the posts by date published

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
   

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog_app/delete_post.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog_app/index.html', context)

def about(request):

    return render(request, 'blog_app/about.html')