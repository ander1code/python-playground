from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name='contents/list.html'

class PersonCreateView(CreateView):
    model = Person
    template_name = "contents/form.html"
    success_url = reverse_lazy('list')


