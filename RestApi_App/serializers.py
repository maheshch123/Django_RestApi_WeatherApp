from .models import weather
from rest_framework import serializers

class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = weather
        fields = '__all__'