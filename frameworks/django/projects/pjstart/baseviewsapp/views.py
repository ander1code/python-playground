from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Person
from .forms import PersonForm


class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    template_name='contents/list.html'

class PersonFormView(View):
    form = PersonForm()
    template_name = 'contents/form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form})

    def post(self, request, *args, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            return redirect('person_list')
        return render(request, self.template_name, {'form':self.form})
