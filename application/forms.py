from django import forms

from django.forms import ModelForm

from .models import Person, Address

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    age = forms.IntegerField(required=False)

class IdForm(forms.Form):
    id = forms.CharField(required=True)


class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'