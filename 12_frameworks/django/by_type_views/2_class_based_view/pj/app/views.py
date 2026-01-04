from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import LoginForm, NaturalPersonForm, NaturalPersonSearchForm
from .models import NaturalPerson
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class ListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = NaturalPersonSearchForm()
        natural_persons = NaturalPerson.objects.all()
        
        paginator = Paginator(natural_persons, 1) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(
            request,
            "persons/natural_person/list.html",
            {
                'natural_persons': page_obj,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = NaturalPersonSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print(f"Name: {search}")
            natural_persons = NaturalPerson.objects.filter(name__istartswith=search)
        else:
            natural_persons = NaturalPerson.objects.all()

        paginator = Paginator(natural_persons, 1) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(
            request,
            "persons/natural_person/list.html",
            {
                'natural_persons': page_obj,
                'form': form
            }
        )

class CreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = NaturalPersonForm()
        return render(request, "persons/natural_person/form.html", {'form': form, 'edition':False})  

    def post(self, request, *args, **kwargs):
        form = NaturalPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created.')
            return redirect(reverse_lazy('natural_person-list'))
        return render(request, "persons/natural_person/form.html", {'form': form, 'edition':False})  


class EditView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        natural_person = get_object_or_404(NaturalPerson,  id=kwargs['id'])
        form = NaturalPersonForm(instance=natural_person)
        return render(request, "persons/natural_person/form.html", {'form': form, 'edition':True})

    def post(self, request, *args, **kwargs):
        natural_person = get_object_or_404(NaturalPerson, id=kwargs['id'])
        if 'delete' in request.POST:
            natural_person.delete()
            messages.success(request, 'Successfully deleted.')
        if 'edit' in request.POST:
            form = NaturalPersonForm(request.POST, request.FILES, instance=natural_person)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully edited.')
            else:
                return render(request, "persons/natural_person/form.html", {'form': form, 'edition':True})
        return redirect(reverse_lazy('natural_person-list'))   

class DetailsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        natural_person = get_object_or_404(NaturalPerson, id=kwargs['id'])
        return render(request, "persons/natural_person/details.html", {'natural_person': natural_person})

class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Sucessfully logout.')
        return redirect(reverse_lazy('login'))

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
            messages.success(request, 'Invalid username and password.')
        return render(request, "login/form.html", {'form':form})

       
        