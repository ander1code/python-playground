
from django.db import models

def validate_gender(gender):
    return gender == "M" or "F"

class Person(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.TextField(max_length=100, null=False)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True
        verbose_name  = 'Person'
        verbose_name_plural = 'People'
        db_table = 'person'
    
class PhysicalPerson(Person):
    gender = models.CharField(null=False, max_length=1, validators=[validate_gender])

    def __str__(self):
        return f"ID: {self.id} | NAME: {self.name} | GENDER: {self.gender} | STATUS: {self.status}"
    
    def __enter__(self):
        return self
    
    def __exit__(self, v1, v2, v3):
        pass

    class Meta:
        verbose_name  = 'Physical_Person'
        verbose_name_plural = 'Physical_People'
        db_table = 'physical_person'

