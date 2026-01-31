from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Student Name', max_length=100)
    contact_no = forms.IntegerField(label='Contact Number')


