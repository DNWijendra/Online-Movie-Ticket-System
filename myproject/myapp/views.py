from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from.forms import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = New_User_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = New_User_Form()
    return render(request,'signup.html',{'form':form})

#admin login
def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=user,password=pwd)
        if user is not None:
            # login(request,user)
            return redirect('Login_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
            # return HttpResponse("username and password are not correct. Try again!")
    return render(request,'login.html')

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

# def edit_movie(request,movie_id):
#     data = Movie.objects.get(movie_id = movie_id)
#     return render(request,'edit_movie.html',{'data':data})

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

# def update_movie(request,movie_id):
#     data = Movie.objects.get(movie_id = movie_id)
#     form = New_Movie_Form(request.POST,request.FILES,instance=data)
#     if form.is_valid():
#         form.save()
#         return redirect('login_home')
#     else:
#         return render(request,'edit_moive.html',{data:data})
    
    # data = get_object_or_404(Movie, pk=movie_id)

    # if request.method == 'POST':
    #     form = New_Movie_Form(request.POST, request.FILES, instance=data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login_home')
    # else:
    #     form = New_Movie_Form(instance=data)
    
    # return render(request, 'edit_movie.html', {'form': form, 'data': data})