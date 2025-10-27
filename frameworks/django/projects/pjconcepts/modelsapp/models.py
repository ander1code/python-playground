from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator
from .validations import *

from django.db import models
from django.utils import timezone
from datetime import timedelta

class BaseClass(models.Model):
    class Meta:
        abstract = True

class PersonQuerySet(models.QuerySet):
    def with_start_name(self, name):
        return self.filter(name__istartswith=name)

    def with_end_name(self, name):
        return self.filter(name__iendswith=name)

    def with_email(self, email):
        return self.filter(email__iexact=email)

    def with_age_above(self, age):
        today = timezone.now().date()
        birth_limit = today - timedelta(days=age * 365)
        return self.filter(birthday__lte=birth_limit)

    def with_age_under(self, age):
        today = timezone.now().date()
        birth_limit = today - timedelta(days=age * 365)
        return self.filter(birthday__gt=birth_limit)
    
    def all(self):
        return self.raw('SELECT * FROM PERSON')

"""
class PersonManager(models.Manager):
    def _get_queryset(self):
        return super().get_queryset()

    def with_start_name(self, name):
        return self._get_queryset().filter(name__istartswith=name)

    def with_end_name(self, name):
        return self._get_queryset().filter(name__iendswith=name)

    def with_email(self, email):
        return self._get_queryset().filter(email__iexact=email)

    def with_age_above(self, age):
        today = timezone.now().date()
        birth_limit = today - timedelta(days=age * 365)
        return self._get_queryset().filter(birthday__lte=birth_limit)

    def with_age_under(self, age):
        today = timezone.now().date()
        birth_limit = today - timedelta(days=age * 365)
        return self._get_queryset().filter(birthday__gt=birth_limit)
"""

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, self._db)

    def with_start_name(self, name):
        return self.get_queryset().with_start_name(name)

    def with_end_name(self, name):
        return self.get_queryset().with_end_name(name)

    def with_email(self, email):
        return self.get_queryset().with_email(email)

    def with_age_above(self, age):
        return self.get_queryset().with_age_above(age)

    def with_age_under(self, age):
        return self.get_queryset().with_age_under(age)
    
    def all(self):
        return self.get_queryset().all()

class BirthdayModel(models.Model):
    birthday = models.DateField(null=True)
    class Meta:
        abstract = True

class NameCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length=50
        self.unique=False
        self.null=True
        self.error_messages={
             'blank': 'Name cannot be empty.',
             'required': 'Name is required.',
             'max_length': 'Name exceeds maximum length of 50 characters.',
        }
        self.validators.append(validate_name)

class Person(BirthdayModel):
    objects = models.Manager()
    manager = PersonManager()
    # queryset =  PersonQuerySet.as_manager()

    GENDERS = (('M','MALE'),('F','FEMALE'),('O','OTHERS'))
    # name = models.CharField("Name", max_length=50, unique=False, null=False,error_messages={
    #         'blank': 'Name cannot be empty.',
    #         'required': 'Name is required.',
    #         'max_length': 'Name exceeds maximum length of 50 characters.',
    #     }, validators=[validate_name])
    name = NameCharField("Name")
    email = models.EmailField(
            "E-mail",
            primary_key=True,
            max_length=50,
            unique=True,
            null=False,
            blank=False,
            validators=[validate_email],
            error_messages={
                'blank': 'Email cannot be empty.',
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
                'unique': 'This email is already in use.',
                'max_length': 'Email exceeds maximum length of 50 characters.',
            }
        )
    description = models.TextField("Description", blank=True, null=True, validators=[MaxLengthValidator(500)], error_messages={
                'max_length': 'Description exceeds the maximum of 500 characters.',
            }
        )
    gender = models.CharField("Gender", max_length=1, choices=GENDERS, default='M', null=False,  validators=[validate_gender], error_messages={
            'blank': 'Gender must be selected.',
            'required': 'Gender is required.',
            'invalid_choice': 'Selected gender is not a valid choice.',
        })
    
    # siblings = models.ManyToManyField("self", on_delete=models.CASCADE, related_name='partner', null=True)

    siblings = models.ManyToManyField("self", related_name='partner')

    address = models.JSONField(null=True)

    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs) 
        print('Successfully saved.')

    def delete(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs) 
        print('Successfully deleted.') 

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['-name']
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        # default_manager_name = 'objects'
        # abstract = True
    
   
class PersonProxy(Person, BaseClass):
    objects = models.Manager()
    manager = PersonManager()

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs) 
        print('Successfully created.')

    def delete(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs) 
        print('Successfully excluded.') 

    def get_description(self):
        print('This is a Proxy Person.')
    
    class Meta:
        proxy = True
        managed = False

    

