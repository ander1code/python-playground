"""
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


# validators:

def validate_birthday(birthday):
    min_age = 18
    limit_birthday = (date.today().year - min_age)
    if birthday > limit_birthday:
        raise ValidationError("Invalid birthday.")

def validate_gender(gender):
    if gender != "M" or gender != "F":
        raise ValidationError("Invalid Gender.")


class Person(models.Model): # classe abstrata e que servirá como modelo
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=False, error_messages={"blank": "Name is empty", "null": "Name is empty", "max-lenght": "Invalid caracter quantity."})
    email = models.EmailField(max_length=100, unique=True, error_messages={"blank": "E-mail is empty", "null": "E-mail is empty", "max-lenght": "Invalid caracter quantity for E-mail.", "unique": "E-mail have must unique."})
    status = models.BooleanField(default=False, error_messages={"blank": "Status is empty", "null": "Status is empty"}) # validar TRUE ou FALSE?

    class Meta:
        ordering = ["name"]
        db_table = "person"
        verbose_name = "Person"
        verbose_name_plural = "People"


class PhysicalPerson(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, db_column="person_id", error_messages={"invalid": "Invalid person selected."})
    birthday = models.DateField(null=False, validators=[validate_birthday], error_messages={"invalid": "Invalid birthday."}) # validar ACIMA DE 18
    gender = models.CharField(max_length=1, null=False, validators=[validate_gender], error_messages={"blank": "Gender is empty", "null": "Gender is empty", "max-lenght": "Invalid caracter quantity for Gender.", "invalid": "Invalid birthday."}) # validar M ou F
    picture = models.BinaryField(unique=True, error_messages={"blank": "Picture is empty", "null": "Picture is empty", "unique": "Picture have must unique."})

    # constructors:

    def __init__():
        pass

    # def __init__(self, id, name, email, status, birthday, gender, picture):
    #     self.id = id
    #     self.name = name
    #     self.email = email
    #     self.status = status
    #     self.birthday = birthday
    #     self.gender = gender
    #     self.picture = picture
    
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "ID is empty.")
        self.name = kwargs.get("name", "Name is empty.")
        self.name = kwargs.get("email", "E-mail is empty.")
        self.status = kwargs.get("status", "Status is empty.")
        self.birthday = kwargs.get("birthday", "Birthday is empty.")
        self.gender = kwargs.get("gender", "Gender is empty.")
        self.name = kwargs.get("picture", "Picture is empty.")

    # override:

    def __str__(self):
        return f"ID: {self.id} | NAME: {self.name} | NAME: {self.email} | NAME: {self.status} | NAME: {self.birthday} | NAME: {self.birthday} | NAME: {self.picture}"

    # META

    class Meta:
        db_table = "physical_person"
        verbose_name = "PhysicalPerson"
        verbose_name_plural = "PhysicalPeople"
"""        

"""
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

# Validators:

def validate_birthday(value):
    min_age = 18
    limit_date = date(date.today().year - min_age, date.today().month, date.today().day)
    if value > limit_date:
        raise ValidationError("Invalid birthday. The person must be at least 18 years old.")

def validate_gender(value):
    if value not in ["M", "F"]:
        raise ValidationError("Invalid gender. Must be 'M' or 'F'.")

class Person(models.Model):  # Classe abstrata que servirá como modelo
    id = models.AutoField(primary_key=True)
    name = models.CharField(
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
        ordering = ["name"]
        db_table = "person"
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.name} ({self.email})"

class PhysicalPerson(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Person, 
        on_delete=models.DO_NOTHING, 
        db_column="person_id", 
        error_messages={"invalid": "Invalid person selected."}
    )
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
    picture = models.ImageField(error_messages={
        "blank": "Picture is empty", 
        "null": "Picture is empty", 
        "unique": "Picture must be unique."
    }, upload_to="picture/")
    
    class Meta:
        db_table = "physical_person"
        verbose_name = "Physical Person"
        verbose_name_plural = "Physical People"

    def __str__(self):
        return f"ID: {self.id} | NAME: {Person.name} | NAME: {Person.email} | NAME: {Person.status} | NAME: {self.birthday} | NAME: {self.birthday} | NAME: {self.picture}"
"""