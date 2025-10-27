from django.db import models
from django.db.models.constraints import UniqueConstraint, CheckConstraint
from django.db.models import Q, F

class Person(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)

    class Meta:
        ordering = ['-name']
        db_table = 'person'
        managed = True
        verbose_name = 'person'
        verbose_name_plural = 'people'

    contraints = [
        UniqueConstraint(fields=['email'], name='unq_person_email'),
        CheckConstraint(check=Q(name__lenght__gt=0), name='chk_person_len_name'  )
    ]

    def __str__(self):
        return self.name
    

    
