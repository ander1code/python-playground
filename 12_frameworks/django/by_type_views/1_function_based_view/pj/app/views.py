from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import LoginForm, NaturalPersonForm, NaturalPersonSearchForm
from .models import NaturalPerson
from .models import NaturalPerson

@login_required(login_url='/login/')
def list(request):
    natural_persons = None
    if request.method == 'POST':
        form = NaturalPersonSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print(f"Name: {search}")
            natural_persons = NaturalPerson.objects.filter(name__istartswith=search)
        else:
            natural_persons = NaturalPerson.objects.all()
    else:
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

@login_required(login_url='/login/')     
def create(request):
    if request.method == 'POST':
        form = NaturalPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created.')
            return redirect(reverse_lazy('natural_person-list'))
    else:
        form = NaturalPersonForm()
    return render(request, "persons/natural_person/form.html", {'form': form, 'edition':False})  

@login_required(login_url='/login/')
def edit(request, id):
    natural_person = get_object_or_404(NaturalPerson, id=id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            natural_person.delete()
            messages.success(request, 'Successfully deleted.')
        if 'edit' in request.POST:
            form = NaturalPersonForm(request.POST, request.FILES, instance=natural_person)
            form.save()
            messages.success(request, 'Successfully edited.')
        return redirect(reverse_lazy('natural_person-list'))   
    else:
        form = NaturalPersonForm(instance=natural_person)
    return render(request, "persons/natural_person/form.html", {'form': form, 'edition':True})

@login_required(login_url='/login/')
def details(request, id):
    print(id)
    natural_person = get_object_or_404(NaturalPerson, id=id)
    return render(request, "persons/natural_person/details.html", {'natural_person': natural_person})

@login_required(login_url='/login/')
def logoff_auth(request):
    logout(request)
    messages.success(request, 'Sucessfully logout.')
    return redirect(reverse_lazy('login'))

def login_auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if not user is None:
                login(request, user)
                messages.success(request, 'Sucessfully login.')
                return redirect(reverse_lazy('natural_person-list'))
    else:
        form = LoginForm()
    return render(request, "login/form.html", {'form':form})

