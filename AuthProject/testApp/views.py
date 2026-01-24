from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm


def home(request):
    return render(request, 'home.html')


@login_required
def python_test(request):
    return render(request, 'python.html')


@login_required
def java_test(request):
    return render(request, 'java.html')


@login_required
def eyc_test(request):
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})
