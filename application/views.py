import csv

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .api.serializers import PersonSerializer

# Path: application\forms.py
from .forms import IdForm, PersonForm, PersonModelForm, AddressModelForm

from .models import Person



def app_home(request):
    """url: /app/"""
    return render(request, 'app/app_home.html')


def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="download.csv"'

    writer = csv.writer(response)

    writer.writerow(['id', 'first_name', 'last_name', 'age'])

    for row in Person.objects.all().values_list('id', 'first_name', 'last_name', 'age'):
        writer.writerow(row)

    return response


@api_view(['GET', 'POST', ])
def get_download(request):
    """ url: /app/get/ """

    if request.method == 'GET':
        form_p = PersonForm()
        form_id = IdForm()
        
        context = {
            'form_p': form_p,
            'form_id': form_id,
        }
        return render(request, 'app/download.html', context)
    
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="download-filter.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'first_name', 'last_name', 'age', 'picture'])


        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        age = request.POST.get('age', None)
        id = request.POST.get('id', None)

        # print('1) ', first_name, last_name, age, id)
        # print ('\nCHAUUUUUU\n')

        try:
            first_name = first_name.title()
        except:
            pass
        try:
            last_name = last_name.title()
        except:
            pass


        if (first_name or last_name or age) and not id:
            # print('2) ', first_name, last_name, age, id)
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

        elif id:
            # buscame los ids que hagan match y descargamelos
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
        print ('\n1)\n\nhola mundoooo!! \n')
        print (persons)
        print ('\n2)\n\nhola mundoooo!! \n')
        print (persons.values)
        print ('\n3)\n\nDIR DE PERSONS(PERSON,)!!!  \n')
        print (dir(persons))
        print ('fin\n\n')
        for row in persons:
            print ('\t============ESTOY DENTRO DE UNA ITERACION!!!')
            print ('\n1)\n\nDIR DE PERSON!! \n')
            print (dir(row))
            print ('\n2)\n\nMIRAME MIRAME MIRAME!! \n')
            # print ([row2 for row2 in row])
            print(row.id)
            print(row.first_name)
            print(row.last_name)
            print(row.age)
            print(row.picture)
            print ('\n3)\n\nFIN \n')
            # writer.writerow(row.objects.all())

        return response


def get(request):
    """ url: /app/get/ """

    if request.method == 'GET':
        form_p = PersonForm()
        form_id = IdForm()
        
        context = {
            'form_p': form_p,
            'form_id': form_id,
        }
    return render(request, 'app/get.html', context)


def post(request):
    """url: get: /app/post/ -> post: /api/v1/person/create/
    ERROR: no debería tener "create"
    """

    context = {}

    if request.user.is_authenticated:
        context['user'] = request.user
    
    if request.method == 'GET':
        form_p = PersonModelForm()
        form_a = AddressModelForm()
        context['form_p'] = form_p
        context['form_a'] = form_a

        return render(request, 'app/post.html', context, status=201)
    return render(request, 'app/post.html', context, status=200)


def id_form(request):
    context = {}
    form_id = IdForm()
    context['form_id'] = form_id
    return render(request, 'app/put.html', context)


    
@api_view(['GET', 'POST'])
def update(request):
    
    context = {}

    id = request.query_params.get('id', None)
    person = get_object_or_404(Person, id=id)

    
    if request.method == 'POST':
        function = request.query_params.get('function', None)
        context['function'] = function

        if function == 'Search':
            form_p = PersonModelForm(request.POST or None, instance=person)
            if form_p.is_valid():
                instance = form_p.save(commit=False)
                clean_data = form_p.cleaned_data
                instance.first_name = clean_data.get('first_name').title()
                instance.last_name = clean_data.get('last_name').title()
                instance.id = clean_data.get('id').replace('.', '').replace('-', '')
                try:
                    instance.picture = request.FILES['picture']
                except:
                    instance.picture = person.picture
                instance.save()
                context['message'] = 'Profile updated successfully'
                return render(request, 'app/update.html', context, status=201)
    
    elif request.method == 'GET':
        form_p = PersonModelForm(instance=person)
        context['form_p'] = form_p
    return render(request, 'app/update.html', context)



@api_view(['GET', 'POST'])
def delete(request):
    context = {}
    
    id = request.query_params.get('id', None)
    person = get_object_or_404(Person, id=id)

    if request.method == 'POST':
        try:
            person.delete()
            context['message'] = 'Person deleted successfully'
            return render(request, 'app/delete.html', context, status=204)
        except Person.DoesNotExist:
            return render(request, 'app/delete.html', context, status=404)

    else:
        form_p = PersonModelForm(instance=person)
        context['form_p'] = form_p
    return render(request, 'app/delete.html', context)