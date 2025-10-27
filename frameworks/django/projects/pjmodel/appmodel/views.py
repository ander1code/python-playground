from django.shortcuts import render, HttpResponse, redirect
from .models import Person
from django.views.decorators.csrf import csrf_protect


def fill(request):
    message = ""
    if Person.objects.count() == 0:
        people = [
            "Amanda Ribeiro",
            "Bruno Carvalho",
            "Camila Duarte",
            "Diego Martins",
            "Elisa Nogueira",
            "Felipe Andrade",
            "Gabriela Costa",
            "Henrique Lima",
            "Isabela Rocha",
            "João Pedro Almeida",
            "Karina Oliveira",
            "Leonardo Freitas",
            "Mariana Teixeira",
            "Nicolas Barros",
            "Priscila Farias",
            "Rafael Monteiro",
            "Sabrina Tavares",
            "Thiago Pinto",
            "Vanessa Moura",
            "Wellington Souza",
            "Beatriz Ramos",
            "Caio Santana",
            "Daniela Pires",
            "Eduardo Cunha",
            "Fernanda Lopes",
            "Gustavo Neves",
            "Helena Braga",
            "Igor Sales",
            "Juliana Castro",
            "Lucas Moreira",
            "Mirela Fontes",
            "Natália Cardoso",
            "Otávio Fernandes",
            "Paula Azevedo",
            "Rodrigo Bastos",
            "Sara Lima",
            "Túlio Mendes",
            "Vitória Camargo",
            "Yasmin Duarte",
            "Anderson Conceição"
        ]; 
    
        for p in people: 
            Person.objects.create(name=p)
        
        message = "Successfully filled!"
    else:
        message = "The database is already was filled!"
    return HttpResponse(message)

def clear(request):
    Person.objects.all().delete()
    return HttpResponse("Successfully cleared!")

def delete(request, id):
    p = Person.objects.filter(id = id)
    p.delete()
    return redirect("index")

def get_person_by_id(request, id):
    id = request.GET.get("id")
    people = Person.objects.filter(pk=id)
    print(people)
    if people.exists():
        return render(request, "contents/list.html", {'people':people})
    else:
        return HttpResponse("Nothing finding!")

def get_person_by_name(request, name):
    name = request.GET.get("name")
    people = Person.objects.filter(name__istartswith=name)
    if people.exists():
        return render(request, "contents/list.html", {'people':people})
    else:
        return HttpResponse("Nothing finding!")

def index(request):
    people = Person.objects.all()
    return render(request, "contents/list.html", {'people':people})

def create(request):
    return render(request, "contents/form.html", {})

def update(request):
    # Person.objects.filter(id=p[1].id).update(name="Anderson da Conceição")
    pass


"""



def __create_list(people):
    names = (
    "<h1>People</h1><br>"
    f"<span style='color:blue;'>Registereds:&nbsp;{people.count()}</span><ul>"
    )

    for p in people:
        names = names + f"<li>{p.name} | <a href='#' onclick=\"if (confirm('Do you want to delete {p.name}?')) window.location.href = '/delete/{p.id}'; return false;\">delete</a></li>"
    names = names + "</ul>"
    return names
    
def show_template(request):
    return render(request, "index.html", {})
"""