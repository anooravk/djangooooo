from django.urls import path
from custom_auth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProfilePictureAPIView
from .views import UserDetailsAPIView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile-picture/', ProfilePictureAPIView.as_view(), name='profile-picture'),
    path('user-details/', UserDetailsAPIView.as_view(), name='user-details'),
]

