from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import LoginForm, NaturalPersonForm, NaturalPersonSearchForm
from .models import NaturalPerson
from .models import NaturalPerson


from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, ListView, DetailView, UpdateView, View

class NaturalPersonListView(LoginRequiredMixin, ListView):
    model = NaturalPerson
    template_name= 'persons/natural_person/list.html'
    paginate_by = 1
    allow_empty = True
    context_object_name = 'natural_persons'
    paginator_class = Paginator
    ordering = ['name']
    login_url = '/login/'

class NaturalPersonCreateView(CreateView):
    model = NaturalPerson
    template_name = 'persons/natural_person/form.html'
    form_class = NaturalPersonForm
    success_url = reverse_lazy('natural_person-list')
    login_url = '/login/'

class NaturalPersonDetailView(DetailView):
    model = NaturalPerson
    context_object_name = 'natural_person'
    template_name = 'persons/natural_person/details.html'

class NaturalPersonUpdateView(UpdateView):
    model = NaturalPerson
    template_name = 'persons/natural_person/form.html'
    form_class = NaturalPersonForm
    success_url = reverse_lazy('natural_person-list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edition"] = True 
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy('natural_person-list'))

    def post(self, request,  *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)
    
class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login/form.html", {'form':form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if not user is None:
                login(request, user)
                messages.success(request, 'Sucessfully login.')
                return redirect(reverse_lazy('natural_person-list'))
        return render(request, "login/form.html", {'form':form})

class LogoffView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Sucessfully logout.')
        return redirect(reverse_lazy('login'))

