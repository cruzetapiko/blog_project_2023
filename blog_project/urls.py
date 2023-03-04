from django.contrib import admin
from django.urls import path, include

from user_app import views as  user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path to django admin
    path('admin/', admin.site.urls),

    #path to blog_app application
    path('', include('blog_app.urls')),

    #user_app paths
    path("register/", user_views.register, name="user_app-register"),
    path("login/", auth_views.LoginView.as_view(template_name='user_app/login.html'), name="user_app-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name="user_app-logout"),
    path("profile/", user_views.profile, name="user_app-profile"),

    #password reset paths
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user_app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user_app/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)