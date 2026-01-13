from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models.constraints import UniqueConstraint, CheckConstraint
from .utils.validators import Validators
from django.db.models import Q

GENDER = (('M','Male'), ('F','Female'), ('O','Other'))

class Person(models.Model):
    
    name = models.CharField(blank=False, null=False, validators=[
        MinLengthValidator(4),
        MaxLengthValidator(50),
    ])

    email = models.CharField(blank=False, null=False, validators=[
        MinLengthValidator(6),
        MaxLengthValidator(50),
    ])

    class Meta:
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        constraints = [
            UniqueConstraint(fields=['email'], name='unq_person_email', violation_error_message='E-mail is already registered.')
        ]

    def __str__(self):
        return f'{self.pk}: {self.name}'


class NaturalPerson(Person):
    
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False, validators=[
        Validators().validate_birthday
    ])
    
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, validators=[
        MinValueValidator(0), 
        MaxValueValidator(9999999999.99),
    ])
    
    gender = models.CharField(blank=False, null=False, choices=GENDER, validators=[
        MinLengthValidator(1),
        MaxLengthValidator(1),
    ])
    
    picture = models.ImageField(upload_to='persons/natural_persons', blank=False, null=False, validators=[
        Validators().validate_picture
    ])

    class Meta:
        db_table = 'natural_person'
        managed = True
        verbose_name = 'NaturalPerson'
        verbose_name_plural = 'NaturalPersons'
        constraints = [
            CheckConstraint(check=(Q(salary__gte=0) or Q(salary__lte=9999999999.99)) , name='chk_natural_person_salary', violation_error_message='Invalid salary.'),
            CheckConstraint(check=Q(gender__in=['M','F','O']), name='chk_natural_person_gender', violation_error_message='Invalid gender.'),
        ]

    def __str__(self):
        return f'{self.pk}: {self.name}' 