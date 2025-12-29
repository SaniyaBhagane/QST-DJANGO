from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    skills = forms.MultipleChoiceField(
        choices=UserProfile.SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = UserProfile
        fields = "__all__"
        widgets = {
            'gender': forms.RadioSelect,
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_skills(self):
        # Convert list → string for DB storage
        return ",".join(self.cleaned_data['skills'])
