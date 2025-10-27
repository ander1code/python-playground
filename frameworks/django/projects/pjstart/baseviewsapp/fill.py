import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjstart.settings')

django.setup()

from .models import Person

p = Person()
print(p)