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



def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="download.csv"'

    writer = csv.writer(response)

    writer.writerow(['id', 'first_name', 'last_name', 'age'])

    for row in Person.objects.all().values_list('id', 'first_name', 'last_name', 'age'):
        writer.writerow(row)

    return response


def get(request):
    form_p = PersonForm()
    form_id = IdForm()
    
    context = {
        'form_p': form_p,
        'form_id': form_id,
    }
    return render(request, 'app/get.html', context)


def post(request):
    
    context = {}

    if request.user.is_authenticated:
        context['user'] = request.user
    
    if request.method == 'POST':
        form_p = PersonModelForm(request.POST or None)
        form_a = AddressModelForm(request.POST or None)
        # FORM VALIDATION
        if form_p.is_valid():
            instance = form_p.save(commit=False)
            clean_data = form_p.cleaned_data
            instance.first_name = clean_data.get('first_name').title()
            instance.last_name = clean_data.get('last_name').title()
            instance.id = clean_data.get('id').replace('.', '').replace('-', '')
            try:
                instance.picture = request.FILES['picture']
            except:
                pass

        elif form_a.is_valid():
            instance = form_a.save(commit=False)
            clean_data = form_a.cleaned_data
            instance.street = clean_data.get('street').title()
            instance.city = clean_data.get('city').title()
        
        context['form_p'] = form_p
        context['form_a'] = form_a
        instance.save()
    
    else:
        form_p = PersonModelForm()
        form_a = AddressModelForm()
        context['form_p'] = form_p
        context['form_a'] = form_a

    return render(request, 'app/post.html', context, status=201)


def put(request):
    context = {}
    
    if request.method == 'POST':
        form_id = IdForm(request.POST or None)
        if form_id.is_valid():
            clean_data = form_id.cleaned_data
            id = clean_data.get('id').replace('.', '').replace('-', '')
            try:
                person = Person.objects.get(id=id)
                context['id'] = id
            except Person.DoesNotExist:
                return render(request, 'app/put.html', context, status=404)

    else:
        form_id = IdForm()
        context['form_id'] = form_id

    return render(request, 'app/put.html', context)


@api_view(['GET', 'POST'])
def update(request):
    
    context = {}

    id = request.query_params.get('id', None)
    person = get_object_or_404(Person, id=id)

    if request.method == 'POST':
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
            # form_p.save()
            #message alert
            context['message'] = 'Person updated successfully'
            return render(request, 'app/update.html', context, status=201)
        
    else:
        form_p = PersonModelForm(instance=person)
        context['form_p'] = form_p
    return render(request, 'app/update.html', context)


def app_home(request):
    return render(request, 'app/app_home.html')
# @api_view(['GET', 'POST'])
# def update(request, id):

#     context = {}

#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'POST':
#         form_p = PersonModelForm(request.POST or None, instance=person)
#         if form_p.is_valid():
#             instance = form_p.save(commit=False)
#             clean_data = form_p.cleaned_data
#             instance.first_name = clean_data.get('first_name').title()
#             instance.last_name = clean_data.get('last_name').title()
#             instance.id = clean_data.get('id').replace('.', '').replace('-', '')
#             try:
#                 instance.picture = request.FILES['picture']
#             except:
#                 instance.picture = None
#                 # instance.picture = person.picture
#             instance.save()
#             form_p.save()
#             # form_p = PersonModelForm(instance=instance).save()

#             serializer = PersonSerializer(instance=person, data=form_p.cleaned_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     else:
#         form_p = PersonModelForm(instance=person)
#         context['form_p'] = form_p
#     return render(request, 'app/update.html', context)