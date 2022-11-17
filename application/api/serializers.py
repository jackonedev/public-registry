from rest_framework.serializers import ModelSerializer

from ..models import Person, Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'