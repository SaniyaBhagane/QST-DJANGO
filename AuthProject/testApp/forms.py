from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control bg-dark text-light border-secondary",
            "placeholder": "Enter your email"
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap styling to all fields
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control bg-dark text-light border-secondary"
            })
