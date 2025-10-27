from django.db import models
from django.db.models import constraints, Q
from django.core.validators import EmailValidator, RegexValidator
from django.db.models.constraints import UniqueConstraint, CheckConstraint
from datetime import date

eighteen_years_ago = date.today().replace(year=date.today().year - 18)

class Person(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0.01)
    gender = models.CharField(max_length=1, blank=False, null=False, choices=GENDER)
    birthday = models.DateField(blank=False, null=False)
    status = models.BooleanField(blank=False, null=False, default=True)

    class Meta:
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['-pk']
        constraints = [
            UniqueConstraint(fields=['email'], name='unq_person_email'),
            CheckConstraint(check=~Q(name=''), name='chk_person_name_not_empty'),
            CheckConstraint(check=Q(salary__gte=0), name='chk_salary_salary_lt_0'),
            CheckConstraint(check=Q(gender__in=['M','F']), name='chk_person_gender'),
            # CheckConstraint(check=Q(birthday__lte=eighteen_years_ago), name='chk_person_birthday'),
            CheckConstraint(check=Q(status__in=[True, False]), name='chk_person_status'),
        ]
    


    