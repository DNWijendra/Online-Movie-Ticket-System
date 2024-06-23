from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from.forms import *
from .models import Movie, BookedSeat
from django.http import JsonResponse
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


def delete_movie(request,movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    movie.delete()
    movies = Movie.objects.all()
    return render(request,'Login_home.html',{'movies':movies})

def edit_movie(request,movie_id):
    data = Movie.objects.get(movie_id = movie_id)
    return render(request,'update_movie',{'data' : data})
    

def update_movie(request,movie_id):
    data = Movie.objects.get(movie_id = movie_id)
    form = New_Movie_Form(request.POST,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect('login_home')
    else:
        return render(request,'edit_moive.html',{data:data})


def booktickets(request):
    movies = Movie.objects.all()
    selected_movie_id = request.GET.get('movie_id')
    selected_movie = None
    if selected_movie_id:
        selected_movie = get_object_or_404(Movie, movie_id=selected_movie_id)

    if request.method == 'POST' and 'card_number' in request.POST:
        movie_id = request.POST.get('movie_id')
        selected_seats_str = request.POST.get('selected_seats')
        selected_seats = [
            {'row': seat[0], 'col': int(seat[1:])}
            for seat in selected_seats_str.split(',') if seat
        ]

        selected_movie = Movie.objects.get(movie_id=movie_id)
        # Save booked seats to the database
        for seat in selected_seats:
            booked_seat, created = BookedSeat.objects.get_or_create(
                row=seat['row'],
                col=seat['col']
            )
            selected_movie.booked_seats.add(booked_seat)
        
        # Show confirmation modal
        context = {
            'movies': movies,
            'selected_movie': selected_movie,
            'show_confirmation': True
        }
        return render(request, "book_tickets.html", context)

    context = {
        'movies': movies,
        'selected_movie': selected_movie,
        'show_confirmation': False
    }
    return render(request, "book_tickets.html", context)

def process_payment(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        selected_seats_str = request.POST.get('selected_seats')
        selected_seats = [
            {'row': seat[0], 'col': int(seat[1:])}
            for seat in selected_seats_str.split(',') if seat
        ]

        selected_movie = Movie.objects.get(movie_id=movie_id)
        # Save booked seats to the database
        for seat in selected_seats:
            booked_seat, created = BookedSeat.objects.get_or_create(
                row=seat['row'],
                col=seat['col']
            )
            selected_movie.booked_seats.add(booked_seat)
        
        return redirect('booktickets')

    return redirect('booktickets')