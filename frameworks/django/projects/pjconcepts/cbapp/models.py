from django.db import models
from django.db.models.constraints import UniqueConstraint, CheckConstraint
from django.db.models import constraints
from django.db.models import Q

class Person(models.Model):
    GENDER = (('F', 'FEMALE'),('M', 'MALE'))
    name = models.CharField("Name", max_length=100, blank=False, null=False)
    email = models.EmailField("E-mail", max_length=50, blank=False, null=False)
    gender = models.CharField("Gender", max_length=1, choices=GENDER, blank=False, null=False) 

    class Meta:
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        constraints = [
            UniqueConstraint(fields=['email'], name='unq_person_email'),
            CheckConstraint(check=Q(gender='M') | Q(gender='F'), name='chk_person_gender')
        ]

    def __str__(self):
        return f'{self.id}: {self.name}' 

    def __unicode__(self):
        return 

