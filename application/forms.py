from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    age = forms.IntegerField(required=False)