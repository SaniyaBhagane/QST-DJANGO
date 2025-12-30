from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        widgets = {
            'gender': forms.RadioSelect,
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.TextInput(attrs={
                'placeholder': 'e.g. Python, Django, HTML'
            }),
        }
