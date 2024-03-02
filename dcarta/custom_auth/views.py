
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer,UserProfileSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDetailsSerializer

class UserDetailsAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer

    def get_object(self):
        return self.request.user

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        profile_picture = self.request.data.get('profile_picture', None)
        request.data['profile_picture'] = profile_picture
        response = super().create(request, *args, **kwargs)
        return response

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class ProfilePictureAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        print("Inside get_object method") 
        try:
            user_profile = UserProfile.objects.get(user=self.request.user)
            return user_profile
        except UserProfile.DoesNotExist:
            print("User profile not found")  
           


