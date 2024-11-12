from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from partners.models import PartnerStatus
from django.contrib.auth import logout
from .forms import ProfileForm

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

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {
        'user': request.user,
        'statuses': PartnerStatus.objects.filter(user=request.user, status='redeemed'), 
    })

@login_required
def profile_settings_view(request):
    user = request.user
    if request.method == 'POST':
        if 'delete_account' in request.POST:
            logout(request)
            user.delete()
            messages.success(request, "Ваш акаунт було видалено.")
            return redirect('home')
        else:
            form = ProfileForm(request.POST, instance=user)
            if 'photo' in request.FILES:
                user.profile.avatar = request.FILES['photo']
            if form.is_valid():
                form.save()
                messages.success(request, "Ваші зміни збережено.")
                return render(request, "profile_set/profile_set.html")
    else:
        form = ProfileForm(instance=user) 

    return render(request, "profile_set/profile_set.html", {'form': form})

def leaderboard_and_statistics_view(request):
    top_users = Profile.objects.filter(level__isnull=False).order_by('-level')[:5]
    completed_tasks = 150  

    return render(request, 'statistics/index.html', {
        'top_users': top_users,
        'completed_tasks': completed_tasks,
    })

def statistics(request):
    return render(request, 'statistics/index.html')


def tasks_view(request):
    return render(request, 'tasks/index.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request) 
        user.delete() 
        messages.success(request, "Your account has been deleted.")
        return redirect('home')  
    return redirect('profile')

