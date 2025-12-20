from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['first_name', 'last_name', 'enrollment_date']
        fields = '__all__'
        
        widget={
            'enrollment_date': forms.DateInput(attrs={'type':'date','placeholder':'Select a date'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'enrollment_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Enrollment Number'}),
            'major': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Major'}),
        }