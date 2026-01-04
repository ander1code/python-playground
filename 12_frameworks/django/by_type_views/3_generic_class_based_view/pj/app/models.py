from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db.models import Q
from django.db.models.constraints import UniqueConstraint, CheckConstraint
from app.utils.validators import Validators

# ------------------------------------------------------------------------------------------------------

GENDERS = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
)
   
# ------------------------------------------------------------------------------------------------------

class Person(models.Model):
    
    name = models.CharField(blank=False, null=False, validators=[
        MinLengthValidator(4), MaxLengthValidator(50)
    ])

    email = models.CharField(blank=False, null=False, validators=[
        MinLengthValidator(6), MaxLengthValidator(50)
    ])

    class Meta:
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        constraints = [
            UniqueConstraint(fields=['email'], name='unq_person_email', violation_error_message='E-mail is already registered.')
        ]

# ------------------------------------------------------------------------------------------------------

class NaturalPerson(Person):

    birthday = models.DateField(blank=False, null=False, validators=[Validators().validate_birthday])
    
    gender = models.CharField(max_length=1, blank=False, null=False, choices=GENDERS, validators=[
        MinLengthValidator(1), MaxLengthValidator(1)
    ])
    
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, validators=[
        MinValueValidator(0.00), MaxValueValidator(9999999999.99)
    ])

    picture = models.ImageField(upload_to='person/natural_person', blank=True, null=True, validators=[Validators().validate_picture])

    def __str__(self):
        return f"{self.pk}: {self.name}" 
    
    class Meta:
        db_table = 'natural_person'
        managed = True
        verbose_name = 'NaturalPerson'
        verbose_name_plural = 'NaturalPersons'
        constraints = [
            CheckConstraint(check=Q(gender__in=['M','F','O']), name='chk_naturalperson_gender', violation_error_message='Invalid gender.'),
            CheckConstraint(check=(Q(salary__gte=0.00) or Q(salary__lte=9999999999.99)), name='chk_naturalperson_salary', violation_error_message='Invalid salary.'),
        ]
    
# ------------------------------------------------------------------------------------------------------

