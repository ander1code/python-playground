from django.shortcuts import render, HttpResponse
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'index.html', {'name':'Anderson'})
    message = _('Hello, World!')
    return HttpResponse(message)
