from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog_app-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='blog_app-user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_app-post-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog_app-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_app-post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='blog_app-post-delete'),
    path('about/',views.about, name='blog_app-about'),
]