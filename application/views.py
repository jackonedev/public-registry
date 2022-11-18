import csv

from django.shortcuts import render
from django.http import HttpResponse


# Path: application\forms.py
from .forms import IdForm, PersonForm, PersonModelForm, AddressModelForm

from .models import Person


def readme(request):
    return render(request, 'readme.html')

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
    return render(request, 'get.html', context)


def post(request):
    
    context = {}
    
    form_p = PersonModelForm(request.POST or None)
    form_a = AddressModelForm(request.POST or None)

    context['form_p'] = form_p
    context['form_a'] = form_a

    if request.user.is_authenticated:
        context['user'] = request.user
    
    if request.method == 'POST':
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
    
        instance.save()
    return render(request, 'post.html', context, status=201)


