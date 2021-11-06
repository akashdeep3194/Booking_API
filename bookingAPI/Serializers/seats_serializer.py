from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, Serializer,SerializerMethodField,StringRelatedField
from bookingAPI.Serializers.movie_serializer import MovieSerializer
from bookingAPI.Serializers.cinema_serializer import CinemasSerializer
from bookingAPI.models.booking_models import Cinema, Movie, Seat, Show

class SeatsSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('show',-1) != -1:
            representation['show'] = self.context['show']
            representation['movie'] = self.context['movie']
        return representation
