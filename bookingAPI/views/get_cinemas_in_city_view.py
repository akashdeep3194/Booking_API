from django.http import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from bookingAPI.Serializers.city_serializer import CitySerializer

from bookingAPI.models.booking_models import Booking,Cinema, City,Movie,Hall,Seat,Show
from bookingAPI.Serializers.cinema_serializer import CinemasSerializer
from bookingAPI.Serializers.shows_serializer import ShowsSerializer

# Create your views here.

class CinemasInCity(APIView):

    def get(self,request:Request,pk=0):
        print(pk)
        city = pk
        if city != 0:
            queryset = get_list_or_404(Cinema,city=city)
            response_data = CinemasSerializer(queryset,many = True)
            return Response(data = response_data.data, status = status.HTTP_200_OK)
        else:
            queryset = get_list_or_404(Cinema)
            response_data = CinemasSerializer(queryset,many = True)
            return Response(data = response_data.data, status=status.HTTP_200_OK)

class ShowsInCinemas(APIView):
    
    def get(self,request:Request,pk=0,cpk=0):
        city = pk
        cinema = cpk
        if city != 0 and cinema != 0:
            queryset = get_list_or_404(Show,cinema=cinema)
            response_data = ShowsSerializer(queryset,many = True)
            return Response(data = response_data.data, status = status.HTTP_200_OK)

# class HallsInCinema(APIView):

#     def get(self,request: Request):
#         cinema = request.data['cinemaid']
