from rest_framework.serializers import ModelSerializer
from bookingAPI.models.booking_models import Cinema, City, Movie

class MovieSerializer(ModelSerializer):



    class Meta:
        model = Movie
        fields = '__all__'
