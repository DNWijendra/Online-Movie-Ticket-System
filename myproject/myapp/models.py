from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=30, null=True)
    ticket_price = models.CharField(max_length=8, null=True)
    image = models.FileField(upload_to='profile', null=True, blank=True)
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


