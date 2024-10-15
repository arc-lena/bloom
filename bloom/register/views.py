from django.shortcuts import render
from .forms import RegisterForm

def sign_up_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(response, "sign_up/index.html", {"form": form})
