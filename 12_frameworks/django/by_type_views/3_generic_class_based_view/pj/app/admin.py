from django.contrib import admin
from .models import NaturalPerson

@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):

    class Meta:
        model = NaturalPerson
        fields = ("name", "email", "birthday", "gender", "salary", "picture")

