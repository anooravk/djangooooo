

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import CardsSerializer
from .models import BusniessCards
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def cardsList(request, format=None):
    if request.method == 'GET':
        cards = BusniessCards.objects.all()
        serializer = CardsSerializer(cards, many=True)
        return Response({"allCards":serializer.data})

    if request.method == 'POST':
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def cardsDetail(request,id,format=None):
    try:
       card = BusniessCards.objects.get(pk=id)
    except BusniessCards.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
      serializer = CardsSerializer(card)
      return Response(serializer.data)
    elif request.method=='PUT':
      serializer = CardsSerializer(card,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
      card.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def exchangedCards(request, user_email,format=None):
    try:
        exchanged_cards = BusniessCards.objects.filter(exchangers__contains=user_email)
    except BusniessCards.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardsSerializer(exchanged_cards, many=True)
        return Response({"exchangedCards":serializer.data})
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userCards(request, user_email, format=None):
    user_cards = BusniessCards.objects.filter(emailAddress=user_email)
    if not user_cards:  
        return Response({"message": "No cards found for the user."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardsSerializer(user_cards, many=True)
        return Response({"userCards":serializer.data})
    
  