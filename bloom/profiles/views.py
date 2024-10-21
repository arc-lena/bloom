from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Зміни на бажану URL-адресу після входу
            else:
                messages.error(request, 'Неправильне ім’я користувача або пароль.')
        else:
            messages.error(request, 'Неправильне ім’я користувача або пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})

@login_required
def info_view(request):
    return render(request, "info/index.html")

def statistics(request):
    return render(request, 'statistics/index.html')