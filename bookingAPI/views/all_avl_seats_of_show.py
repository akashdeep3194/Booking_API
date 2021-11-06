from django.http import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from bookingAPI.Serializers.seats_serializer import SeatsSerializer

from bookingAPI.models.booking_models import Booking,Cinema, City,Movie,Hall,Seat,Show
from bookingAPI.Serializers.shows_serializer import ShowsSerializer

# Create your views here.

class AllSeatsofAShow(APIView):
    
    def get(self,request:Request,spk=0):
        show = spk
        if show != 0:
            # queryset = get_list_or_404(Show, movie=mpk)

            qshow = get_object_or_404(Show,pk=spk)
            print("\n\n qshow: ",qshow)
            hid = qshow.hall_id
            print("\n\n hid: ",hid)
            # qs = Seat.objects.filter(hall=hid) #----------------------------------
            # show_bookings = Booking.objects.filter(show=spk)
            # seat_id_list = []

            # for each_booking in show_bookings:
            #     print(each_booking.seat.id)
            #     seat_id_list.append(each_booking.seat.id)
            # qss = Seat.objects.exclude(id__in = seat_id_list).filter(hall=hid)
            qss2 = Seat.objects.filter(hall=hid).exclude(booking__show=spk, booking__confirmed = False)
            movie_name = qshow.movie.movie_name
            print(movie_name)
            response_data = SeatsSerializer(qss2,context = {"show":spk, "movie":movie_name},many = True)

            return Response(data = response_data.data, status = status.HTTP_200_OK)
        else:
            return Response(data="Invalid Show")
