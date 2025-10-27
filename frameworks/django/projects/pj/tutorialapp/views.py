from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from django.template import loader
from django.views.generic import ListView, DetailView

from .models import Person

"""
def index(request):
    template = loader.get_template("contents/list.html")
    people = Person.objects.order_by("-name")
    context = {'people':people}
    return HttpResponse(template.render(context=context, request=request))
"""
    
# def index(request):
#     people = Person.objects.all()
#     return render(request, "contents/list.html", {'people':people})

"""
def details(request, id):
    template = loader.get_template("contents/details.html")
    try:
        person = Person.objects.filter(pk=id)
        context = {'person':person}
    except Person.DoesNotExist:
        raise Http404("Not found!")
    return HttpResponse(template.render(context=context, request=request))
"""

# def details(request, id):
#     person =  get_object_or_404(Person.objects.filter(pk=id))
#     return render(request, "contents/details.html", {'person':person})


class PersonListView(ListView):
    model = Person
    template_name = "contents/list.html"
    context_object_name = "people"
    
class PersonDetailView(DetailView):
    model = Person
    template_name = "contents/details.html"
    context_object_name = "person"

def delete(request, id):
    pass