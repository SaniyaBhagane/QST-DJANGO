from django.shortcuts import render
from django.generic.view import View

# Create your views here.

class HelloView(View):
    def get(self, request):
        return render(request, 'hello.html')