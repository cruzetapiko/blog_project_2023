from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path to django admin
    path('admin/', admin.site.urls),

    #path to blog_app application
    path('admin/', include('blog_app.urls')),

    
]
