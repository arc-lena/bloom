from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def sign_up_view(request):
    return render(request, 'sign-up/index.html')


def login_view(request):
    return render(request, 'login/index.html')
