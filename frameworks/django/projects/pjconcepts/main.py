import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjconcepts.settings')
django.setup()

from modelsapp.models import Person, PersonProxy



