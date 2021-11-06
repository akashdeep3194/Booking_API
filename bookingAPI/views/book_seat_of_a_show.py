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

class BookSeatOfAShow(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request:Request,shpk=0,sepk=0):

        show = shpk
        seat = sepk
        if show != 0 and seat != 0:

            queryset_show = Show.objects.filter(pk = shpk)
            queryset_seat = Seat.objects.filter(pk = sepk)

            if len(queryset_seat) == 0 or len(queryset_show) == 0:
                return Response(data="Bad Request seat invalid or Show invalid", status=status.HTTP_400_BAD_REQUEST)

            if (queryset_seat[0].hall.id != queryset_show[0].hall.id):
                print("Bad Requst")
                return Response(data = "Bad Request seat not in show", status=status.HTTP_400_BAD_REQUEST)

            user_id = request.user.id
            payload=dict()


            payload["show"] = shpk
            payload["cinema"] = queryset_show[0].cinema.id
            payload["seat"] = sepk
            payload["movie"] = queryset_show[0].movie.id
            payload["hall"] = queryset_show[0].hall.id
            payload["user"] = user_id
            payload["confirmed"] = False


            show_booking = Booking.objects.filter(show=shpk,seat=sepk)
            if len(show_booking) == 0:
                serialized_payload = BookingSerializer(data = payload)
                
                if serialized_payload.is_valid():

                    # Block a booking till payment is made successfully
                    serialized_payload.save()
                    

                    # call payment service and store result in is_payment_done


                    #Simulating a payment scenario that may fail as well

                    list_bool = [True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,]
                    is_payment_done = random.choice(list_bool) 

                    # 15/16 times payment would be successful 1/16 times payment would be unsuccessful

                    if is_payment_done == True:

                        payload["confirmed"] = True
                        show_booking_final = Booking.objects.filter(show=shpk,seat=sepk)
                        serialized_payload_final  = BookingSerializer(show_booking_final[0], data=payload)
                        if serialized_payload_final.is_valid():
                            serialized_payload_final.save()
                            return Response(data=serialized_payload_final.data, status = status.HTTP_201_CREATED)
                        else:
                            return Response(data = serialized_payload_final.errors,status=status.HTTP_400_BAD_REQUEST)
                    else:
                        show_booking_final = Booking.objects.filter(show=shpk,seat=sepk)
                        show_booking_final.delete()
                        show_booking.delete()
                        return Response(data = "Payment Failed!",status=status.HTTP_409_CONFLICT)
                else:
                    return Response(data="something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                response_data = BookingSerializer(show_booking, many = True)
                for ele in response_data.data:
                    ele.pop("user") # Remove user details from booking information
                return Response(data = ["Seat is already booked"] + response_data.data , status=status.HTTP_409_CONFLICT)

        else:
            return Response(data="Invalid Show or Seat",status=status.HTTP_400_BAD_REQUEST)
