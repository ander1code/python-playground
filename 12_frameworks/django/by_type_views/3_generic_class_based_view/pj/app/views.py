import os
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from .forms import LoginForm, NaturalPersonForm, NaturalPersonSearchForm
from .models import NaturalPerson

base_templates = 'persons/natural_person/'
login_templates = 'login'

class NaturalPersonListView(LoginRequiredMixin, ListView):
    model = NaturalPerson
    template_name = os.path.join(base_templates, 'list.html')
    context_object_name = 'natural_persons'
    paginate_by = 1
    login_url = '/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = NaturalPersonSearchForm(self.request.GET)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            if search:
                queryset = queryset.filter(name__istartswith=search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NaturalPersonSearchForm() 
        context["natural_persons"] = context["page_obj"] # apenas para mudar o nome.
        return context
    
class NaturalPersonCreateView(LoginRequiredMixin, CreateView):
    model = NaturalPerson
    template_name =  os.path.join(base_templates, 'form.html')
    form_class = NaturalPersonForm
    success_url = reverse_lazy('natural_person_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(NaturalPersonCreateView, self).get_context_data(**kwargs)
        context['edition'] = False
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully created.')
        return super().form_valid(form)
    
class NaturalPersonDetailView(LoginRequiredMixin, DetailView):
    model = NaturalPerson
    template_name = os.path.join(base_templates, 'details.html')
    context_object_name = 'natural_person'
    login_url = '/login/'

class NaturalPersonUpdateView(LoginRequiredMixin, UpdateView):
    model = NaturalPerson
    template_name = os.path.join(base_templates, 'form.html')
    context_object_name = 'natural_person'
    pk_url_kwarg = "pk"
    form_class = NaturalPersonForm
    success_url = reverse_lazy('natural_person_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edition"] = True
        return context
    
    def post(self, request, *args, **kwargs):
        if 'delete' in self.request.POST:
            object = self.get_object()
            object.delete()
            messages.success(request, 'Successfully deleted.')
            return redirect('natural_person_list')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Successfully edited.')
        return reverse_lazy('natural_person_details', kwargs={'pk':self.object.id} )
            
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, os.path.join(login_templates, 'form.html'), {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if not user is None:
                login(request=request, user=user)
                messages.success(request, 'Successfully logged.')
                return redirect(reverse_lazy('natural_person_list'))
            else:
                messages.error(request, 'Invalid username and password.')
        form = LoginForm()
        return render(request, os.path.join(login_templates, 'form.html'), {'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request=request)
        messages.success(request, 'Successfully logout.')
        return redirect('login')
    
    
    




    

