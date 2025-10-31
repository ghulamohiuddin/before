from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from . import models

CustomUser = get_user_model()

USED_EMAILS = ["test@example.com", "hello@example.com"]


class PasswordForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        label="Your Email",
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    password = forms.CharField(
        required=True,
        label="password",
        widget=forms.PasswordInput(attrs={"placeholder": "input password"}),
        min_length=8,
        max_length=14,
        help_text="password must be 8 digit long",
    )

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long ")

        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one number ")

        return password
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email in USED_EMAILS:  
            raise forms.ValidationError("This email is already used.")
        return email
