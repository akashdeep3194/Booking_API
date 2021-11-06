from django.http import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request

from bookingAPI.models.booking_models import Booking,Cinema, City,Movie,Hall,Seat,Show
from bookingAPI.Serializers.shows_serializer import ShowsSerializer

# Create your views here.

class ShowsOfMovieInCity(APIView):
    
    def get(self,request:Request,mpk=0,cpk=0):
        movie = mpk
        city = cpk
        if city != 0 and movie != 0:
            # queryset = get_list_or_404(Show, movie=mpk)
            qs = Show.objects.filter(movie=mpk, cinema__city=cpk)
            response_data = ShowsSerializer(qs,many = True)
            return Response(data = response_data.data, status = status.HTTP_200_OK)
        else:
            return Response(data="Invalid City or Movie")
