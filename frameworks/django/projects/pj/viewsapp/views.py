from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView,View
from .models import Person

class Example02TemplateView(TemplateView):

    template_name = 'contents/template_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Olá, Mundo!'
        return context
    
def index(request):
    return render(request, 'contents/home.html', {})

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name='crud/list.html'

class PersonDirectDeleteView(View):
    def get(self, request, pk):
        p = get_object_or_404(Person, pk=pk)
        p.delete()
        return redirect('person_list')