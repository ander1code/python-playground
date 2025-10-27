from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Person

def index(request):
    return render(request, 'contents/hello.html', {'message':'Olá, mundo!'})

def condition(request):
    return render(request, 'contents/conditions.html', {'age':23})

def greeting(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    else:
        name = ''
    return render(request, 'contents/form.html', {'name':name})

def looping(request):
    people = ['fernanda', 'lissa', 'tania', 'paula', 'jane', 'carol', 'amanda', 'anne']
    return render(request, 'contents/loopings.html', {'people': people, 'numbers': range(0,101,5)})

def json(request):
    _json = {
        "user": {
            "id": 1,
            "name": "João Silva",
            "email": "joao.silva@example.com",
            "is_active": True,
            "registered_at": "2025-09-15T14:00:00Z"
        },
        "preferences": {
            "language": "pt-BR",
            "notifications": {
            "email": True,
            "sms": False
            }
        },
        "last_login": "2025-09-15T14:25:00Z"
        }
    return JsonResponse(_json)

def redirect_to_google(request):
    return redirect("https://www.google.com.br")

def register(request):
    if request.method == 'POST':
        _name = request.POST.get('name')
        Person(name=_name).save()
    _people = Person.objects.all()
    return render(request, 'contents/register.html', {'people':_people})

def delete(request, _id):
    _person = get_object_or_404(Person, id=_id)
    _person.delete()
    return redirect("register")

"""
def details(request, _id):
    _person = Person.objects.filter(id = _id)
    print(_person.name)
    return render(request, 'contents/details.html', {'person':_person})
"""

def details(request, _id):
    _person = get_object_or_404(Person, id=_id)
    print(_person.name)
    return render(request, 'contents/details.html', {'person': _person})

def custom_500_view(request):
    return render(request, '500.html', status=500)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)