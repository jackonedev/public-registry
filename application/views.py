from django.http import HttpResponse
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

# @api_view(['GET'])
# def getPerson(request,first_name):#TODO='', lname='', age=''):
#     persons = Person.objects.filter(first_name=first_name)
#     serializer = PersonSerializer(persons, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def getPerson(request):
    first_name = request.query_params.get('first_name', None)
    last_name = request.query_params.get('last_name', None)
    age = request.query_params.get('age', None)

    persons = Person.objects.filter(first_name=first_name, last_name=last_name, age=age)
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getPersonById(request):
    id = request.query_params.get('id', None)

    if not id.startswith('*') and not id.endswith('*'):
        persons = Person.objects.filter(id=id)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    else:
        return HttpResponse("Not implemented yet")