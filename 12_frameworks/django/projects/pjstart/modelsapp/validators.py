from django.core.exceptions import ValidationError
from datetime import date
import re

def validate_gender(gender):
    gender = gender.strip().upper()
    genders = ['M','F','O']
    if not gender:
        raise ValidationError("Gender is empty.")
    if gender not in genders:
        raise ValidationError("Invalid gender.")
    
def validate_birthday_to_register(birthday):
    if not birthday:
        raise ValidationError("Birthday is empty.")    
    today = date.today()
    today_eighteen_ago = date(today.year - 18, today.month, today.day)
    if birthday > today_eighteen_ago:
        raise ValidationError("Invalid birthday.")    
    
# def validate_salary(salary):
#     if not salary:
#         raise ValidationError("Salary is empty.")
#     if salary < 0:
#         raise ValidationError("Invalid salary.")

def validate_salary(salary):
    pass

def validate_email(email):
    if not email:
        raise ValidationError("E-mail is empty")
    # pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # if not re.match(pattern, email):
    #     raise ValidationError("Invalid E-mail.")