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
    # path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    
    path('user/login/', views.user_login, name='user_login'),
    path('admin_m/login/', views.admin_login, name='admin_login'),
    path('admin_m/signup/', views.admin_signup, name='admin_signup'),
    path('user/signup/', views.user_signup, name='user_signup'),
    path('user_home/', views.user_home, name='user_home'),
    path('Login_home/', views.Login_home, name='Login_home'),
    path('logout/', views.logout, name='logout'),
    path('addmovie/', views.add_movie, name='addmovie'),
    path('booktickets/', views.booktickets, name='booktickets'),
    path('deletemovie/<int:movie_id>', views.delete_movie, name='deletemovie'),
    path('editmovie/<int:movie_id>', views.edit_movie, name='editmovie'),
    path('updatemovie/<int:movie_id>', views.update_movie, name='updatemovie'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('view_profile/', views.view_profile, name='view_profile')
]

# Adding static and media URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
