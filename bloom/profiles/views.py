from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/index.html')


@login_required
def profile_view(request):
    profile = request.user.profile  # Отримує профіль пов'язаний з користувачем
    return render(request, 'profile.html', {'profile': profile})