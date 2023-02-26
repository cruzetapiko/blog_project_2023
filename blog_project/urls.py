from django.contrib import admin
from django.urls import path, include

from user_app import views as  user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path to django admin
    path('admin/', admin.site.urls),

    #path to blog_app application
    path('', include('blog_app.urls')),

    #user_app paths
    path("login/", auth_views.LoginView.as_view(template_name='user_app/login.html'), name="user_app-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name="user_app-logout"),
    path("profile/", user_views.profile, name="user_app-profile"),
]