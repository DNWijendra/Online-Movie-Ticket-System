from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from.forms import *

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.utils import timezone

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
    today = timezone.now().date()
    now_showing_movies = Movie.objects.filter(release_date__lte=today)
    context = {
        'movies': now_showing_movies,
    }
    return render(request, 'user_home.html', context)

def home(request):
    now_screening_movies = Movie.objects.filter(screening_type='Now Screening')
    coming_soon_movies = Movie.objects.filter(screening_type='Coming Soon')
    context = {
        'now_showing_movies': now_screening_movies,
        'coming_soon_movies': coming_soon_movies,
    }
    return render(request, 'home.html', context)

#admin login home to add/remove/edit content
def Login_home(request):
    movies = Movie.objects.all()
    return render(request,'Login_home.html',{'movies':movies})

def logout(request):
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

def booktickets(request):
    now_showing_movies = Movie.objects.filter(screening_type='Now Screening')
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
        
        # Calculate total ticket price
        total_ticket_price = len(selected_seats) * 1000  # Assuming Rs. 1000 per ticket

        # Show confirmation modal
        context = {
            'movies': now_showing_movies,
            'selected_movie': selected_movie,
            'show_confirmation': True,
            'total_ticket_price': total_ticket_price
        }
        return render(request, "book_tickets.html", context)

    context = {
        'movies': now_showing_movies,
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