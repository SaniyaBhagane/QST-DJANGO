from django.shortcuts import render
from .models import todo
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

# Create your views here.
class AddTask(CreateView):
    model = todo
    fields = '__all__'
    template_name = "create_form.html"
    success_url = '/home/'

class Home(ListView):
    model = todo
    template_name = "home.html"
    
class DeleteTask(DeleteView):
    model = todo
    success_url = '/home/'