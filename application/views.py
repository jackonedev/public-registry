from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from application import serializers

from django.shortcuts import render

from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer


def home(request):
    return render(request, 'home.html')



@api_view(['GET'])
def getAllPerson(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPerson(request):
    first_name = request.query_params.get('first_name', None)
    last_name = request.query_params.get('last_name', None)
    age = request.query_params.get('age', None)

    if first_name and last_name and age:
        persons = Person.objects.filter(first_name=first_name, last_name=last_name, age=age)

    elif first_name and last_name:
        persons = Person.objects.filter(first_name=first_name, last_name=last_name)
    
    elif first_name and age:
        persons = Person.objects.filter(first_name=first_name, age=age)

    elif last_name and age:
        persons = Person.objects.filter(last_name=last_name, age=age)
    
    elif first_name:
        persons = Person.objects.filter(first_name=first_name)

    elif last_name:
        persons = Person.objects.filter(last_name=last_name)

    elif age:
        persons = Person.objects.filter(age=age)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPersonById(request):
    id = request.query_params.get('id', None)
    
    if not id:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if not id.startswith('*') and not id.endswith('*'):
        persons = Person.objects.filter(id=id)

    elif id.startswith('*') and id.endswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__icontains=id)

    elif id.startswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__iendswith=id)

    elif id.endswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__istartswith=id)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)