from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "person"

class Car(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100, null=False)
    plate = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "car"


