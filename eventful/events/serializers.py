from rest_framework import serializers
from .models import Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields='__all__'

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields='__all__'


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField(child=serializers.EmailField())



