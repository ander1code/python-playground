from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, World!")
    # raise Exception("This is a error!!!")

def index_without_login(request):
    return HttpResponse("Hello, World! (index_without_login)")
    # raise Exception("This is a error!!!")

def error_404(request, exception):
    return render(request, "errors/404.html", status=404)

def error_500(request):
    return render(request, "errors/500.html", status=500)