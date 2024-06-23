from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from.forms import *

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Login_home')
    else:
        form = UserCreationForm()
    return render(request, 'admin_signup.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user_signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = New_User_Form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = New_User_Form()
#     return render(request,'signup.html',{'form':form})

#admin login
def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=user,password=pwd)
        if user is not None:
            return redirect('Login_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request,'login.html')

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=user, password=pwd)
        if user is not None and user.is_active and not user.is_staff:
            login(request, user)
            return redirect('user_home')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials'})
    return render(request, 'user_login.html')

def admin_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=user, password=pwd)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('Login_home')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

def user_home(request):
    # movies = Movie.objects.all()
    return render(request,'user_home.html')

def home(request):
    movies = Movie.objects.all()
    return render(request,'home.html',{'movies':movies})

#admin login home to add/remove/edit content
def Login_home(request):
    movies = Movie.objects.all()
    return render(request,'Login_home.html',{'movies':movies})

def user_logout(request):
    return redirect('home')

def add_movie(request):
    if request.method == 'POST':
        form = New_Movie_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Login_home')
    else:
        form = New_Movie_Form()
    return render(request,"add_movie.html",{'form':form})

def booktickets(request):
    return render(request,"book_tickets.html")

def delete_movie(request,movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    movie.delete()
    movies = Movie.objects.all()
    return render(request,'Login_home.html',{'movies':movies})

def edit_movie(request, movie_id):
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    form = New_Movie_Form(instance=movie_instance)
    return render(request, 'edit_movie.html', {'form': form, 'movie_id': movie_id})

def update_movie(request, movie_id):
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'POST':
        form = New_Movie_Form(request.POST, request.FILES, instance=movie_instance)
        if form.is_valid():
            form.save()
            return redirect('Login_home')
    else:
        form = New_Movie_Form(instance=movie_instance)
    
    return render(request, 'edit_movie.html', {'form': form, 'movie_id': movie_id})
