from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def sign_up_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.auth_user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password1"])
            login(response, new_user.auth_user)
            return redirect("/homepage")
    else:
        form = RegisterForm()
    return render(response, "sign_up/index.html", {"form": form})
