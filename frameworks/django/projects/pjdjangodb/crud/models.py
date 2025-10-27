from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

# Validators:

def validate_birthday(value):
    raise ValidationError("Invalid birthday. The person must be at least 18 years old.")
    # min_age = 18
    # limit_date = date(date.today().year - min_age, date.today().month, date.today().day)
    # if not value > limit_date:
    #     raise ValidationError("Invalid birthday. The person must be at least 18 years old.")

def validate_gender(gender):
    if (gender != "M") or (gender != "F"):
        raise ValidationError("Invalid gender. Must be 'M' or 'F'.")

class Person(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)
    
    name = models.TextField(
        max_length=100, 
        null=False, 
        error_messages={
            "blank": "Name is empty", 
            "null": "Name is empty", 
            "max_length": "Invalid character quantity."
        }
    )

    email = models.EmailField(
        max_length=100, 
        unique=True, 
        error_messages={
            "blank": "E-mail is empty", 
            "null": "E-mail is empty", 
            "max_length": "Invalid character quantity for E-mail.", 
            "unique": "E-mail must be unique."
        }
    )

    status = models.BooleanField(
        default=False, 
        error_messages={
            "blank": "Status is empty", 
            "null": "Status is empty"
        }
    )
    
    class Meta:
        abstract = True
        db_table = "person"
        verbose_name = "Person"
        verbose_name_plural = "People"

class PhysicalPerson(Person):

    birthday = models.DateField(
        null=False, 
        validators=[validate_birthday], 
        error_messages={"invalid": "Invalid birthday."}
    )

    gender = models.CharField(
        max_length=1, 
        null=False, 
        validators=[validate_gender], 
        error_messages={
            "blank": "Gender is empty", 
            "null": "Gender is empty", 
            "max_length": "Invalid character quantity for Gender.", 
            "invalid": "Invalid gender."
        }
    )

    picture = models.ImageField(
        error_messages={
            "blank": "Picture is empty", 
            "null": "Picture is empty", 
            "unique": "Picture must be unique."
        }, 
        upload_to="picture/"
    )
    
    class Meta:
        ordering = ["name"]
        db_table = "physical_person"
        verbose_name = "Physical Person"
        verbose_name_plural = "Physical People"

    def __str__(self):
        return f"ID: {self.id} | NAME: {self.name} | EMAIL: {self.email} | STATUS: {self.status} | BIRTHDAY: {self.birthday} | GENDER: {self.gender} | PICTURE: {self.picture}"

    def __enter__(self):
        return self
    
    def __exit__(self, v1, v2, v3):
        pass


