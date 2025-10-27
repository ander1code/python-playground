from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.conf.urls import handler400

def index(request):
    return render(request, "contents/home.html", {})

def fill_database(request):
    if Person.objects.count() > 0:
        people = [
            "João Silva",
            "Maria Oliveira",
            "Pedro Souza",
            "Ana Lima",
            "Carlos Pereira",
            "Beatriz Costa",
            "Lucas Rocha",
            "Fernanda Martins",
            "Mateus Almeida",
            "Larissa Fernandes",
            "Gabriel Barbosa",
            "Juliana Cardoso",
            "Rafael Ribeiro",
            "Camila Monteiro",
            "Tiago Moreira",
            "Patrícia Azevedo",
            "Bruno Freitas",
            "Renata Cunha",
            "André Gomes",
            "Tatiane Teixeira",
            "Rodrigo Dias",
            "Vanessa Pires",
            "Eduardo Nascimento",
            "Letícia Ramos",
            "Felipe Correia",
            "Débora Mendes",
            "Gustavo Farias",
            "Natália Batista",
            "Marcelo Castro",
            "Isabela Andrade",
            "Leandro Coelho",
            "Mariana Rezende",
            "Vitor Neves",
            "Aline Moura",
            "Diego Tavares",
            "Elaine Barros",
            "Otávio Macedo",
            "Cintia Silveira",
            "Henrique Antunes",
            "Tatiana Queiroz",
            "Sérgio Brito",
            "Viviane Xavier",
            "Daniel Siqueira",
            "Priscila Lopes",
            "Igor Braga",
            "Paula Vasconcelos",
            "Jonathan Dorneles",
            "Simone Assis",
            "Vinícius Fonseca",
            "Luciana Guimarães"
        ]

        for p in people:
            Person(name=p).save()
        
        message = "Successfully filled!"
    else:
        message = "Already filled!"

    return HttpResponse(message)


def hello(request):
    return HttpResponse('Hello, World!')

def error_404(request, exception):
    return render(request, "errors/404.html", {})

def redirect_google(request):
    return redirect("https://www.google.com.br")

def show_json_data(request):
    data = {
        "nome": "João Silva",
        "idade": 30,
        "email": "joao.silva@example.com",
        "ativo": True,
        "enderecos": [
            {
                "tipo": "residencial",
                "logradouro": "Rua das Flores",
                "numero": 123,
                "cidade": "São Paulo",
                "estado": "SP"
            },
            {
                "tipo": "comercial",
                "logradouro": "Av. Paulista",
                "numero": 1000,
                "cidade": "São Paulo",
                "estado": "SP"
            }
        ]
    }
    return JsonResponse(data)

from django.views.generic import ListView, FormView
from .models import Person

from .forms import PersonForm

from django.urls import reverse_lazy

class PersonListView(ListView):
    model = Person
    template_name = "people/list.html"
    context_object_name = "people"

class PersonFormView(FormView):
    template_name = "people/form.html"
    form_class = PersonForm
    success_url = reverse_lazy('form-success')

    def form_valid(self, form):
        form.cleaned_data