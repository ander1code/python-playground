from django.db import models
from django.core.exceptions import ValidationError

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


