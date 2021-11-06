from rest_framework.serializers import ModelSerializer
from bookingAPI.models.booking_models import Cinema, City

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
