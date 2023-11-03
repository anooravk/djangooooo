"""
URL configuration for eventful project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from events import views
# from custom_auth import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')), #adds login and register endpoints
    path('email/',views.emailSender), #sends email
    path('allevents/',views.eventsList), #all events
    path('allevents/<int:id>/',views.eventsDetail), #one event by its event id
    path('host-status/', views.checkHostStatus),
    path('event-status/<str:event_status>/', views.eventStatus), #events of diff status
    path('user-events/<str:user_email>/<str:event_status>/', views.userEvents), #user events of diff status
    path('all-user-events/<str:user_email>/', views.userAllEvents), #user events of all status
    path('hosted-events/<str:user_email>/', views.hostedEvents), #events by host email
    path('attended-events/<str:user_email>/', views.userAttendedEvents), #events attended by email
]

urlpatterns = format_suffix_patterns(urlpatterns)

