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
        return Response(status=404)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getPersonById(request):
    id = request.query_params.get('id', None)

    if not id.startswith('*') and not id.endswith('*'):
        persons = Person.objects.filter(id=id)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif id.startswith('*') and id.endswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__icontains=id)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif id.startswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__iendswith=id)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif id.endswith('*'):
        id = id.replace('*', '')
        persons = Person.objects.filter(id__istartswith=id)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    else:#
        return Response(status=404)