from django import forms
class StudentForm(forms.Form):
    sid = forms.IntegerField(label='Student ID')
    sname = forms.CharField(label='Student Name', max_length=100)
    sage = forms.FloatField(label='Student Age')
    
class AdvancedStudentForm(forms.Form):
    feedback = forms.CharField(
        label='Feedback',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Enter your feedback here...'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    document = forms.FileField(
        label='Upload Document'
    )
    profile_picture = forms.ImageField(
        label='Upload Profile Picture'
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    agree_terms = forms.BooleanField(
        required=True,
        label='I agree to the terms and conditions'
    )