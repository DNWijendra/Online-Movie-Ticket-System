from django.db import models

class Movie(models.Model):
    MOVIE_TYPES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
        ('musical fantasy', 'Musical Fantasy'),
        ('other', 'Other'),
    ]

    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('sinhala', 'Sinhala'),
        ('tamil', 'Tamil'),
        ('hindi', 'Hindi'),
    ]

    SCREENING_CHOICES = [
        ('Now Screening', 'Now Screening'),
        ('Coming Soon', 'Coming Soon'),
    ]

    SHOW_TIMES = [
        ('10 AM', '10 AM'),
        ('12 PM', '12 PM'),
        ('4 PM', '4 PM'),
        ('7 PM', '7 PM'),
        ('10 PM', '10 PM'),
    ]

    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=30, null=True)
    ticket_price = models.CharField(max_length=8, null=True)
    image = models.FileField(upload_to='profile', null=True, blank=True)
<<<<<<< HEAD
    show_time = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=10, null=True)
    language = models.CharField(max_length=10, null=True)
    release_date = models.CharField(max_length=10, null=True)
    screening_type = models.CharField(max_length=20, null=True)
    booked_seats = models.ManyToManyField('BookedSeat', blank=True)

    def __str__(self):
        return self.movie_name

class BookedSeat(models.Model):
    row = models.CharField(max_length=1)
    col = models.IntegerField()

    def __str__(self):
        return f"{self.row}{self.col}"


=======
    show_time = models.CharField(max_length=15, choices=SHOW_TIMES, null=True)
    type = models.CharField(max_length=20, choices=MOVIE_TYPES, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, null=True)
    release_date = models.DateField(null=True)
    screening_type = models.CharField(max_length=20, choices=SCREENING_CHOICES, null=True)

    def __str__(self):
        return self.movie_name
>>>>>>> 88df72d6177384df391cc8b6cd9f45053b515c80
