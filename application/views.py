from rest_framework.response import Response
from rest_framework.decorators import api_view
from application import serializers

from django.shortcuts import get_object_or_404

from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer


@api_view(['GET'])
def getAllPerson(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPerson(request):
    persons = Person.objects.all()
    data = request.data
    print (data)
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)