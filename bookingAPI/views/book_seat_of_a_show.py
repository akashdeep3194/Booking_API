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

# Create your views here.

class BookSeatOfAShow(APIView):
    
    def get(self,request:Request,shpk=0,sepk=0):

        show = shpk
        seat = sepk
        if show != 0 and seat != 0:

            queryset = Show.objects.filter(pk = shpk)

            user_id = request.user.id
            payload=dict()

            payload["show"] = shpk
            payload["cinema"] = queryset[0].cinema.id
            payload["seat"] = sepk
            payload["movie"] = queryset[0].movie.id
            payload["hall"] = queryset[0].hall.id
            payload["user"] = 1
            payload["confirmed"] = False

            show_booking = Booking.objects.filter(show=shpk,seat=sepk)
            if len(show_booking) == 0:
                serialized_payload = BookingSerializer(data = payload)
                
                if serialized_payload.is_valid():
                    serialized_payload.save()
                    # call payment service
                
                    is_payment_done = False

                    if is_payment_done == True:
                        show_booking_final = Booking.objects.filter(show=shpk,seat=sepk)
                        payload_final = dict()
                        payload_final["confirmed"] = True
                        serialized_payload_final  = BookingSerializer(show_booking_final, data=payload)
                        if serialized_payload_final.is_valid():
                            return Response(data=serialized_payload_final.data, status = status.HTTP_201_CREATED)
                        else:
                            return Response(data = serialized_payload_final.errors,status=status.HTTP_400_BAD_REQUEST)
                    else:
                        show_booking_final = Booking.objects.filter(show=shpk,seat=sepk)
                        show_booking_final.delete()
                        return Response(data = "Payment Failed!",status=status.HTTP_409_CONFLICT)
                else:
                    return Response(data="something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                response_data = BookingSerializer(show_booking, many = True)
                return Response(data = ["Seat is already booked"] + response_data.data , status=status.HTTP_409_CONFLICT)

        else:
            return Response(data="Invalid Show or Seat",status=status.HTTP_400_BAD_REQUEST)
