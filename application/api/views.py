from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from application.models import Person
from application.api.serializers import PersonSerializer, AddressSerializer


@api_view(['GET', ])
def getAllPerson(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def getPerson(request):
    first_name = request.query_params.get('first_name', None).title()
    last_name = request.query_params.get('last_name', None).title()
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
    if len(persons) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def getPersonById(request):
    id = request.query_params.get('id', None)
    
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
    if len(persons) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
def createPerson(request):
    data = request.data
    if request.method == 'POST':
        person = Person.objects.create(
            id=data['id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age']
        )
        try:
            person.picture = request.FILES['picture']
            person.save()
        except:
            pass
    
    serializer = PersonSerializer(person, many=False)
    try:
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def updatePerson(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def deletePerson(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = person.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)

# @api_view(['GET', ]) 
# def api_details_person_view(request, id):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)