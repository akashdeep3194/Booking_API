from django.db import models
from django.db.models.deletion import CASCADE,DO_NOTHING,RESTRICT,PROTECT
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.TextField(verbose_name='City Name')
    state = models.TextField(verbose_name="State",null=True)


class Movie(models.Model):
    movie_name = models.TextField(verbose_name='Movie Name')
    movie_details = models.TextField(verbose_name="Additional data", null=True)

    # def __str__(self):
    #     return str(self.movie_name)

class Cinema(models.Model):
    address = models.TextField(verbose_name='Cinema Address')
    # city = models.TextField(verbose_name='City')
    city = models.ForeignKey(City, on_delete=CASCADE)

class Hall(models.Model):
    cinema = models.ForeignKey(Cinema,on_delete=CASCADE)
    hall_name = models.TextField(verbose_name="Hall name")
    capacity = models.IntegerField(verbose_name='Hall Capacity')

    # def __str__(self):
    #     return str(self.hall_name)

class Seat(models.Model):
    hall = models.ForeignKey(Hall,on_delete=CASCADE)
    type = models.TextField(verbose_name="Seat Type")

class Show(models.Model):
    show_time = models.TimeField(verbose_name='Show Time')
    movie = models.ForeignKey(Movie,on_delete=CASCADE)
    hall = models.ForeignKey(Hall,on_delete=CASCADE)
    cinema = models.ForeignKey(Cinema,on_delete=CASCADE)

class Booking(models.Model):
    seat = models.ForeignKey(Seat,on_delete=CASCADE)
    show = models.ForeignKey(Show,on_delete=CASCADE)
    movie = models.ForeignKey(Movie,on_delete=CASCADE)
    hall = models.ForeignKey(Hall,on_delete=CASCADE)
    cinema = models.ForeignKey(Cinema,on_delete=CASCADE)
    user = models.ForeignKey(User, verbose_name="Username", on_delete=DO_NOTHING) # donothing
