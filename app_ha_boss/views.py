from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from .forms import PasswordForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Password
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
def Password_view(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if Password.objects.filter(email=email).exists():
                form.add_error("email", "This email is already registered.")
            else:
                Password.objects.create(name=name, email=email, password=password)
                return render(request, "accounts/password.html", {
                    "form": PasswordForm(),
                    "success": True,
                })
    else:
        form = PasswordForm()

    return render(request, "accounts/password.html", {"form": form})