from django.db import models

class Person(models.Model):
    GENDER = {
        'F': 'Female',
        'M': 'Male'
    }
    name = models.CharField(max_lenght=100)
    birthday = models.DateField()
    gender = models.CharField(max_lenght=1, choices=GENDER)

class Car(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE) 
    name = models.CharField(max_lenght=45)
    plate = models.CharField(max_lenght=7, unique=True)


