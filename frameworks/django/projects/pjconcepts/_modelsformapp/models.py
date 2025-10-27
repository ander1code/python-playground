from django.db import models
from django.utils.timezone import now
from django.db.models import UniqueConstraint
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class Person(models.Model):
    name = models.CharField(
        "Name", 
        max_length=50, 
        blank=False, 
        null=False,
        error_messages={
            'blank': 'Name is empty.',
        }
    )
    email = models.EmailField(
        "E-mail", 
        max_length=50, 
        # unique=True, 
        blank=False, 
        null=False, 
        error_messages={
            'blank': 'E-mail is empty.',
            'unique': 'E-mail already registered.',
        }
    )
    created_at = models.DateTimeField(
        "Created At", 
        default=now, 
        blank=False, 
        null=False,
        error_messages={
            'blank': "'Created At' is empty.",
            'null': "'Created At' is empty.",
        }
    )

    class Meta:
        ordering = ['-created_at']
        db_table = 'person'
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        constraints = [
            UniqueConstraint(fields=['email'], name='unq_person_email'),
        ]

    def __str__(self):
        return f"{self.id}: {self.name} - {self.email} - {self.created_at}"
 
    