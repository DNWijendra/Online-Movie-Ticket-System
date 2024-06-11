"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('Login_home/', views.Login_home, name='Login_home'),
    path('logout/', user_logout, name='logout'),
    path('addmovie/', views.add_movie, name='addmovie'),
    path('booktickets/', views.booktickets, name='booktickets'),
    path('deletemovie/<int:movie_id>', views.delete_movie, name='deletemovie'),
    path('editmovie/<int:movie_id>', views.edit_movie, name='editmovie'),
    path('updatemovie/<int:movie_id>', views.update_movie, name='updatemovie')
]

# Adding static and media URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
