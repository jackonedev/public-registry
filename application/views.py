from rest_framework.response import Response
from rest_framework.decorators import api_view
from application import serializers

from django.shortcuts import get_object_or_404

from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer


@api_view(['GET'])
def person_list(request):
    persons = get_object_or_404(Person.objects.all())
    # persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)