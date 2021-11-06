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

# Create your views here.

class Cities(APIView):

    def get(self,request:Request,pk = 0):

        if pk == 0:
            queryset = get_list_or_404(City)
            response_data = CitySerializer(queryset,many = True)
            return Response(data = response_data.data,status=status.HTTP_200_OK)

        else:
            print(pk)
            queryset = get_list_or_404(City,pk=pk)
            response_data = CitySerializer(queryset,many = True)
            return Response(data = response_data.data, status = status.HTTP_200_OK)

