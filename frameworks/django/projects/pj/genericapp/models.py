from django.db import models

class Person(models.Model):
    name = models.CharField(max_lenght=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    birthday = models.DateField(null=False)
    picture = models.ImageField(null=False)
    status = models.BooleanField(null=False)
    
    def __str__(self):
        return self.name
    