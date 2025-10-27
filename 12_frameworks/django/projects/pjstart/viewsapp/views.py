from django.shortcuts import render, HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from django.http import HttpResponseNotFound, Http404
from modelsapp.models import Person

from django.views.decorators.http import require_http_methods

people = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Kleber", "Larissa", "Marcos", "Natália", "Otávio",
    "Paula", "Rafael", "Sabrina", "Thiago", "Vanessa"
]

# Create your views here.
def index(request):
    return render(request, 'contents/home.html', {})

def search_cep(request, cep):
    return HttpResponse(cep)

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_403(request, exception=None):
    return render(request, '403.html', status=403)

def greeting(request, name):
    return HttpResponse(f'Hello, {name}!')

def check_age(request, age):
    if age >= 18:
        return HttpResponse(f'Adult!')
    if age >= 14 and age < 18:
        return HttpResponse(f'Teen!')
    else:
        return HttpResponse(f'Child!')
    
def hello_from_project_url(request):
    return HttpResponse('Hello, World! (PJ)')

@require_http_methods(['GET'])
def greeting_to_html(request, name):
    return render(request, 'contents/greeting.html', {'name': name})

def execute_list_iteration(request):
    return render(request, 'contents/iteration.html', {'people': people})

"""
def greeting_redirect(request, name):
    return HttpResponseRedirect(reverse('greeting_to_html'), kwargs={'name':name})
"""

# ------------------------
# Escrevendo 'views':
# ------------------------

def show_sample_view(request, current_time):
    hello_html = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Hello World</title>
            <style>
                body {{
                    background-color: #f0f4f8;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }}

                h1 {{
                    color: #2c3e50;
                    font-size: 48px;
                }}

                p {{
                    color: #555;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>Welcome to your first page with embedded HTML and CSS.</p>
            <p>{current_time}</p>
        </body>
        </html>
    """
    return HttpResponse(hello_html)


def find_person_in_people_by_name(request, name):
    if name in people:
        return HttpResponse(f'{name} was found!')
    else:
        return HttpResponseNotFound(f'{name} not found!')
    
def get_person_by_id(request, id):
    try:
        person = Person.manager.get(pk=id)
    except Person.DoesNotExist:
        raise Http404('Person not found!!!!')
    return render(request, 'contents/details.html', {'person':person})

"""
async def current_datetime(request):
    from datetime import datetime
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
"""

from django.http import HttpResponseNotAllowed

@require_http_methods(['POST'])
def execute_post(request):
    return HttpResponse(f'Post executed!')

from django.shortcuts import render
from .forms import UploadForm
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_protect
def upload_file(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'contents/form_upload.html', {'form':form})


from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name="dispatch")
class ViewWithDecorator(View):
    def post(self, request, *args, **kwargs):
        return JsonResponse({'status':'Ok!'})
    
    def get(self, request, *args, **kwargs):
        return render(request, 'contents/form_view.html', {})

from django.shortcuts import get_object_or_404
def get_person_details_01(request, id):
    person  = get_object_or_404(Person, pk=id)
    return render(request, 'contents/details.html', {'person':person})

def get_person_details_02(request, id):
    try:
        person = Person.manager.get(pk=id)
    except Person.DoesNotExist as error:
        print(f'Error: {error}')
        raise Http404('Person not found!!!')
    return render(request, 'contents/details.html', {'person':person})
    
"""
    “Views” de base:
        View
        TemplateView
        RedirectView
        
        Views de exibição genéricas
            DetailView
            ListView
        
        Views de edição genérica
            FormView
            CreateView
            UpdateView
            DeleteView
"""