from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, RedirectView

class HelloWorldTemplateView(TemplateView):
    template_name = "contents/hello1.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, World!'
        return context

class MyRedirectView(RedirectView):
    permanent = False
    url = "https://www.youtube.com"

    def get_redirect_url(self, *args, **kwargs):
        print("Successfully redirected.")
        return super().get_redirect_url(*args, **kwargs)

def to_redirect(self):
    return HttpResponse("Successfully redirected.")
  
   
# ----------------------------------------------------------------------------- #
# CRUD
# ----------------------------------------------------------------------------- #

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView
from .models import Person
from django.urls import reverse_lazy
from .forms import PersonForm 

"""
class PersonIndex(TemplateView):
    template_name = 'crud/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        return context
"""

class PersonIndex(ListView):
    template_name = 'crud/index.html'
    model = Person
    paginate_by = 1 # quantos quero que apareça por pagina
    context_object_name = 'people'
    # queryset = Person.objects.all()

    def get_queryset(self):
        return Person.objects.all()
    
class PersonMaleIndex(ListView):
    template_name = 'crud/index.html'
    model = Person
    paginate_by = 1 # quantos quero que apareça por pagina
    context_object_name = 'people'
    
    def get_queryset(self):
        return Person.objects.filter(gender__exact='M')
    
"""
class PersonDetail(DetailView):
    model = Person
    template_name='crud/details.html'
    context_object_name = 'person'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = self.object
        return context
"""

class PersonDetail(DetailView):
    model = Person
    template_name='crud/details.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

"""
class PersonCreateFormView(FormView):
    template_name='crud/form.html'
    form_class = PersonForm
    success_url = reverse_lazy('person-index')

    # com isso que começou a salvar!!!
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""

class PersonCreateFormView(CreateView):
    template_name='crud/form.html'
    model = Person
    fields = ['name','email','gender']
    # form_class = PersonForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('person-index')

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = 'Enter a name.'
        initial['email'] = 'Enter a e-mail.'
        return initial
    

class PersonUpdateView(UpdateView):
    template_name='crud/form.html'
    model = Person
    fields = ['name','email','gender']
    # form_class = PersonForm
    success_url = reverse_lazy('person-index')

  
    

    
# ----------------------------------------------------------------------------- #