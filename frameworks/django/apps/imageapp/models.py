from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

def validation_birthday(birthday):
    if (birthday.year > date.today().year - 18):
        raise ValidationError("Invalid birthday(model)!")

class Person(models.Model):
    name = models.CharField(max_length=100, null=False)
    birthday = models.DateField(null=False, validators=[validation_birthday])
    picture = models.ImageField(default="picture.jpg", null=False)

    def __str__(self):
        return f"Name: {self.name} |Picture: {self.picture}" 
    
    def __enter__(self):
        return self 

    def __exit__(self, v1, v2, v3):
        pass

    class Meta:
        ordering = ["name"]
        db_table = "person"
        verbose_name = "Person"
        verbose_name_plural = "People"

    
