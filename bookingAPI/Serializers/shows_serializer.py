from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer,SerializerMethodField,StringRelatedField
from bookingAPI.Serializers.movie_serializer import MovieSerializer
from bookingAPI.Serializers.cinema_serializer import CinemasSerializer
from bookingAPI.models.booking_models import Cinema, Movie, Show

class ShowsSerializer(ModelSerializer):
    movie = SlugRelatedField(slug_field='movie_name',read_only = True)
    hall = SlugRelatedField(slug_field='hall_name', read_only = True)
    cinema = SlugRelatedField(slug_field='address', read_only = True)
    city_name = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ("id", "show_time","movie","hall",'cinema','city_name')
    def get_city_name(self,obj:Show):
        return obj.cinema.city.name