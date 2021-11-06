from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from bookingAPI.models.booking_models import Cinema, City, Movie, Booking

class BookingSerializer(ModelSerializer):

    movie_name = serializers.SerializerMethodField()
    show_time = serializers.SerializerMethodField()
    cinema_address = serializers.SerializerMethodField()
    hall_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'
    def get_movie_name(self,obj:Booking):
        return obj.movie.movie_name
    def get_cinema_address(self,obj:Booking):
        return obj.cinema.address
    def get_hall_name(self,obj:Booking):
        return obj.hall.hall_name
    def get_show_time(self,obj:Booking):
        return obj.show.show_time
    