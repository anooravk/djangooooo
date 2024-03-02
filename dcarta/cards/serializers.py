from rest_framework import serializers
from .models import BusniessCards


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model= BusniessCards
        fields='__all__'
