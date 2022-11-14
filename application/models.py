from django.db import models


class Person(models.Model):
    id = models.CharField('DNI', max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    #picture = models.ImageField(upload_to='media/person', blank=True)

    def __str__(self) -> str:
        s = "{} {}, dni: {}"
        return s.format(self.first_name, self.last_name, self.id)


class Address(models.Model):
    street = models.CharField(max_length=30)
    number = models.IntegerField()
    city = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        s = "{}, {} {}, {}"
        return s.format(self.person, self.street, self.number, self.city)