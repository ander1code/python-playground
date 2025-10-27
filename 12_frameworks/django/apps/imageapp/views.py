from django.shortcuts import render, redirect
from .forms import MyForm
from .models import *


def index(request):
    people = Person.objects.all()
    return render(request, "list.html", {"people":people})

def create(request):
    if request.method == "POST":
        myform = MyForm(request.POST, request.FILES)
        if myform.is_valid():
            with Person() as p:
                p.name = myform.cleaned_data["name"]
                p.picture = myform.cleaned_data["picture"]
                p.birthday = myform.cleaned_data["birthday"]
                p.full_clean() # para chamar os validators do Model.
                p.save()
            return redirect(index)
    else:
        myform = MyForm()
    return render(request, "create.html", {"form":myform})