from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import LoginForm

from django.contrib import messages

@login_required(login_url='login')
def index(request):
    return render(request, 'contents/hello.html', {})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username and password.')
        return render(request, 'login/login.html', {'form': form})

def auth_logout(request):
    logout(request)  # para deslogar
    return redirect('login')
