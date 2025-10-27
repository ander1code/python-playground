from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def view1(request):
    template = loader.get_template("app1/page1.html")
    context = {"name":"Anderson"}
    return HttpResponse(template.render(template, context))
    
def view2(request):
    context = {"name":"Anderson"}
    return render(request, "app1/page2.html", context)


