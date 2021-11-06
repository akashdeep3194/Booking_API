from rest_framework.serializers import ModelSerializer
from bookingAPI.models.booking_models import Cinema

class CinemasSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'
