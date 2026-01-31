from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Student Name', max_length=100)
    ContactNo = forms.IntegerField(label='Contact Number')


