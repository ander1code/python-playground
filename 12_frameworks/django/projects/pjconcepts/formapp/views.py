from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib import messages

def index(request):
    people = Person.objects.all()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Successfully created.')
            form = PersonForm()
    else:
        form = PersonForm()
    return render(request, 'contents/form.html', {'form':form, 'people':people})


def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    messages.success(request=request, message='Successfully deleted.')
    return redirect('index')