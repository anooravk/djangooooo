from django.shortcuts import render
from django.db.models import Q
from .models import Event,User
from .serializers import EventsSerializer,UsersSerializer,EmailSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


@api_view(['POST'])
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

       


@api_view(['GET','POST'])
def usersList(request,format=None):
    if request.method=='GET':
      users = User.objects.all()
      serializer = UsersSerializer(users,many=True)
      return Response(serializer.data)
    
    if request.method=='POST':
      serializer = UsersSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      
@api_view(['GET','PUT','DELETE'])
def usersDetail(request,id,format=None):
    try:
       user =   User.objects.get(pk=id)
    except Event.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
      serializer = UsersSerializer(user)
      return Response(serializer.data)
    elif request.method=='PUT':
      serializer = EventsSerializer(user,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
      user.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def eventsList(request,format=None):
    if request.method=='GET':
      events = Event.objects.all()
      serializer = EventsSerializer(events,many=True)
      return Response(serializer.data)
    
    if request.method=='POST':
      serializer = EventsSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      


@api_view(['GET','PUT','DELETE'])
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
def eventStatus(request,event_status, format=None):
    try:
        active_events = Event.objects.filter(status=event_status)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(active_events, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def userEvents(request, user_email,event_status, format=None):
    try:
        user_events = Event.objects.filter( Q(invitees__contains=user_email) & Q(status=event_status))
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def userAllEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(invitees__contains=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def userAttendedEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(attendees__contains=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def hostedEvents(request, user_email, format=None):
    try:
        user_events = Event.objects.filter(hostEmail=user_email)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSerializer(user_events, many=True)
        return Response(serializer.data)