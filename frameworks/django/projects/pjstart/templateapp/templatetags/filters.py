from django import template
import math

register = template.Library()

@register.filter(name='convert_to_uppercase')
def convert_to_uppercase(value):
    return value.upper()

@register.filter(name='cube')
def cube(value):
    return value ** 3
