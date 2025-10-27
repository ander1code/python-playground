from django.http import JsonResponse, HttpResponse
from .models import *

def index(request):
    people = PhysicalPerson.objects.all()
    return HttpResponse(people)

def create(request):
    if request.method == "POST":
      try:
        with PhysicalPerson() as pp:
          pp.name = request.POST.get("name")
          pp.gender = request.POST.get("gender")
          pp.status = request.POST.get("status")
          pp.save()
        return HttpResponse("Sucessfully created.")
      except Exception:
        return HttpResponse("Error creating.")

def details(request, id):
    print("hdjash jdash jdash dash djash djashkj")
    if request == "GET":
      try:
        pp = PhysicalPerson.objects.get(pk=id)
        print(pp)
        return HttpResponse(pp)
      except Exception:
        return HttpResponse("Error detailing.")

def edit(request, id, name, gender, status):
    if request == "PUT":
      try:
        with PhysicalPerson().objects.get(pk=id) as pp:
          pp.id = id
          pp.name = name
          pp.gender = gender
          pp.status = status
          pp.save()
        return HttpResponse("Sucessfully edited.")
      except Exception:
        return HttpResponse("Error editing.")

    if request == "DELETE":
      try:
        pp = PhysicalPerson().objects.get(pk=id)
        pp.delete()
        return HttpResponse("Sucessfully deleted.")
      except Exception:
        return HttpResponse("Error deleting.")

    



