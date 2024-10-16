from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login_view(request):
    return render(request, 'login/index.html')


def info_view(request):
    return render(request, "info/index.html")

