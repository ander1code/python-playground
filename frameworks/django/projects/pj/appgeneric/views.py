from django.shortcuts import render, get_object_or_404, redirect
from .models import Person

# basicão!
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import PersonForm

class PersonListView(ListView):
    model = Person
    template_name='crud/list.html'

class PersonCreateView(CreateView):
    model = Person
    
    # comento os campos, e passo a referenciar o formulario de forms.py
    # fields = ['name']
    form_class = PersonForm
    
    template_name = "crud/form.html"
    success_url = reverse_lazy('list')

class PersonUpdateView(UpdateView):
    model = Person

    # comento os campos, e passo a referenciar o formulario de forms.py
    # fields = ['name']
    form_class = PersonForm

    template_name = "crud/form.html"
    success_url = reverse_lazy('list')
    
class PersonDeleteView(DeleteView):
     model = Person
     template_name = 'crud/confirm_delete.html'
     success_url = reverse_lazy('list')

class PersonDetailView(DetailView):
    model = Person
    template_name='crud/detail.html'

# excluindo diretamente:
class PersonDeleteDirectView(View): # trabalhando com view padrão!
    # nao precisa implementar os dois:
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return redirect('list')
    
    def post(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return redirect('list')
    