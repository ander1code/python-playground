from django.shortcuts import render
from django.http import Http404


# person

class Crud:
    people = [
        {"id":1, "name":"Anderson"},
        {"id":2, "name":"Fernanda"},
        {"id":3, "name":"Renata"},
        {"id":4, "name":"Luiza"},
        {"id":5, "name":"Paula"},
        {"id":6, "name":"Bianca"},
        {"id":7, "name":"Nathalia"},
    ]

def index(request):
    context = {"people":Crud.people}
    return render(request, "crud/person/index.html", context)    
    
def create(request):
    if request.POST:
        Crud.people += {"id":request.get("id"), "name":request.get("name")}
        return render(request, "crud/person/index.html", {})    
    return render(request, "crud/person/create.html", {})    

def details(request, id):
    return render(request, "crud/person/details.html", {})    

def edit(request, id):
    return render(request, "crud/person/edit.html", {})    

# login

def login(request):
    return render(request, "crud/login/login.html", {})    

