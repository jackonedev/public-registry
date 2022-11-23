from django import forms

from django.forms import ModelForm

from .models import Person, Address

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False, label='Name' ,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

class IdForm(forms.Form):
    id = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'id': 'DNI',
            'first_name': 'Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'picture': 'Select picture',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'id': 'DNI',
            'street': 'Street',
            'number': 'Number',
            'city': 'City'
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }

    # def clean_id(self):
    #     id = self.cleaned_data.get('id')
    #     if id:
    #         id = id.replace('.', '').replace('-', '')
    #         if not id.isnumeric():
    #             raise forms.ValidationError('DNI must be numeric')
    #     return id
