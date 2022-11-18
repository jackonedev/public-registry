from django.shortcuts import render

from .forms import IdForm, PersonForm, PersonModelForm, AddressModelForm


def home(request):
    form_p = PersonForm()
    form_id = IdForm()
    
    #TODO: VALIDATE FORMS
    
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


