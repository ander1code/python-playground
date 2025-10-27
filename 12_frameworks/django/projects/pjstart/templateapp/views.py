from django.shortcuts import render, HttpResponse
from datetime import date
from django.views.generic import TemplateView, View

def index(request):
    return render(request, 'contents/filter_view.html', {'message':'hello, World!', 'current_date':date.today()})

from django.views import View

import asyncio

class MyTemplateView(TemplateView):
    template_name = 'contents/hello2.html'

class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(5)
        return HttpResponse('(Async) Hello, World!')
   
def translate_page(request):
    return render(request, 'contents/translate.html', {})

class DefaultView(View):
    message = 'Default Message!'
    def get(self, request):
        return HttpResponse(self.message)
    
class HelloWorldView(DefaultView):
    message = 'Hello, World!'

def view_test(request):
    if request.method == 'POST':
        return HttpResponse('POST!!!')
    else:
        return HttpResponse('GET!!!')