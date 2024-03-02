from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

class RegisterSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(write_only=True, required=False)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','profile_picture')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),  
            last_name=validated_data.get('last_name', '') 
        )

        user.set_password(validated_data['password'])
        user.save()
        profile_picture = validated_data.pop('profile_picture', None)
        user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture)
        return user



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = RegisterSerializer(instance=self.user)
        try:
            user_profile = UserProfile.objects.get(user=self.user)
            profile_serializer = UserProfileSerializer(instance=user_profile)
            data['profile_picture'] = profile_serializer.data['profile_picture']
        except UserProfile.DoesNotExist:
            data['profile_picture'] = None
        data['email'] = serializer.data['email']
        data['username'] = serializer.data['username']
        return data

class UserDetailsSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture', 'date_joined')

    def get_profile_picture(self, user):
        try:
            user_profile = UserProfile.objects.get(user=user)
            return UserProfileSerializer(instance=user_profile).data['profile_picture']
        except UserProfile.DoesNotExist:
            return None