from django.shortcuts import render
from django.http import HttpResponse    
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Beer

# Create your views here.

# CLASS BASED VIEW: way of writing views in Django using Python classes instead of functions. CBVs help you organize code better, reuse logic, and handle common web patterns easily.


class HelloView(View):
    def get(self, request):
        return HttpResponse("<h2>Hello, World! This is a class-based view response.</h2>")
    
    # def post(self, request):
    #     return HttpResponse("<h2>This is a POST request response from the class-based view.</h2>")
    # used to handle POST requests for api calls need postman or insomnia tool 
    
    # def put(self, request):
    #     return HttpResponse("<h2>This is a PUT request response from the class-based view.</h2>")   
    # used to handle PUT requests for api calls need postman or insomnia tool
    
    # def delete(self, request):
    #     return HttpResponse("<h2>This is a DELETE request response from the class-based view.</h2>")
    # used to handle DELETE requests for api calls need postman or insomnia tool
    
class TemplateView(TemplateView):
    template_name = "sample.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Django"
        context['course'] = "CBV Class Based Views"
        context['duration'] = "2 months"
        return context
    
class AddBeer(CreateView):
    model = Beer
    fields = '__all__'
    template_name = 'beer_form.html'
    
class BeerList(ListView):
    model = Beer
    context_object_name = 'beers'
    template_name = 'beer_list.html'
     
class ViewBeer(DetailView):
    model = Beer
    context_object_name = 'beer'
    template_name = 'beer_detail.html'
    
class UpdateBeer(UpdateView):
    model = Beer
    fields = '__all__'
    template_name = 'beerUpdate_form.html'
    
class DeleteBeer(DeleteView):
    model = Beer
    success_url = '/list/'
    template_name = 'beer_confirm_delete.html'