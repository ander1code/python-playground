from django.contrib import admin
from .models import NaturalPerson

class NaturalPersonAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'salary', 'birthday', 'gender', 'picture')
    list_display =  ('name', 'email', 'salary', 'birthday', 'gender', 'picture')
    ordering =  ('name', )

admin.site.register(NaturalPerson, NaturalPersonAdmin)

