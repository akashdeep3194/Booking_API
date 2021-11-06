from django.http import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from bookingAPI.Serializers.booking_serializer import BookingSerializer
from bookingAPI.Serializers.seats_serializer import SeatsSerializer

from bookingAPI.models.booking_models import Booking,Cinema, City,Movie,Hall,Seat,Show
from bookingAPI.Serializers.shows_serializer import ShowsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import random


# Create your views here.

class AllBookingsOfAUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request:Request):

        user_id = request.user.id
        qs = Booking.objects.filter(user = user_id)
        count = qs.count()
        serialized_data_qs = BookingSerializer(qs,many=True)

        if len(qs) != 0:
            return Response(data = [{"Your Total Bookings": count}] + serialized_data_qs.data,status=status.HTTP_200_OK)
        else:
            return Response(data="No Bookings by the user",status=status.HTTP_200_OK)
