from django.shortcuts import render
from django.views.generic import View
# Create your views here.
 
def NavView(request):
    return render(request, 'navbar.html')

# @login_re
def pythonView(request):
    return render(request, 'pyt.html')
