from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from application import serializers

from django.shortcuts import render

from .forms import IdForm, PersonForm, PersonModelForm, AddressModelForm

from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer


def home(request):
    form_p = PersonForm()
    form_id = IdForm()
    context = {
        'form_p': form_p,
        'form_id': form_id,
    }
    return render(request, 'home.html', context)

def post(request):
    
    context = {}
    
    form_p = PersonModelForm(request.POST or None)
    form_a = AddressModelForm(request.POST or None)

    context['form_p'] = form_p
    context['form_a'] = form_a

    if request.user.is_authenticated:
        context['user'] = request.user
    
    if request.method == 'POST':
        if form_p.is_valid():
            instance = form_p.save(commit=False)
            clean_data = form_p.cleaned_data
            instance.first_name = clean_data.get('first_name').title()
            instance.last_name = clean_data.get('last_name').title()
            instance.id = clean_data.get('id').replace('.', '').replace('-', '')
            instance.save()

        if form_a.is_valid():
            instance = form_a.save(commit=False)
            clean_data = form_a.cleaned_data
            instance.street = clean_data.get('street').title()
            instance.city = clean_data.get('city').title()
            instance.save()

    return render(request, 'post.html', context)
    
    

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

    if len(persons) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
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