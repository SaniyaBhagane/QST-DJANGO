from django import forms
class StudentForm(forms.Form):
    sid = forms.IntegerField(label='Student ID')
    sname = forms.CharField(label='Student Name', max_length=100)
    sage = forms.FloatField(label='Student Age')