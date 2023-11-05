
from django.conf import settings
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import EventsSerializer,EmailSerializer
from .models import Event
from django.core.mail import send_mail
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkHostStatus(request):
    user = request.user
    ishost = user.ishost
    return Response({'ishost': ishost})


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def eventsList(request, format=None):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def eventsDetail(request,id,format=None):
    try:
       event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
      serializer = EventsSerializer(event)
      return Response(serializer.data)
    elif request.method=='PUT':
      serializer = EventsSerializer(event,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
      event.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def eventStatus(request,event_status, format=None):
    try:
        active_events = Event.objects.filter(status=event_status)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(active_events, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userEvents(request, user_email,event_status, format=None):
    try:
        user_events = Event.objects.filter( Q(invitees__contains=user_email) & Q(status=event_status))
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userAllEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(invitees__contains=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response({"events":serializer.data})
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userAttendedEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(attendees__contains=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def hostedEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(hostEmail=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response({"events":serializer.data})
    
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def emailSender(request, format=None):
    if request.method == 'POST':
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data.get('subject')
            message = serializer.validated_data.get('message')
            recipient_list = serializer.validated_data.get('recipient_list')
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



