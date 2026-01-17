from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# authproject1234

def home(request):
    return render(request, 'home.html')


@login_required
def python_test(request):
    return render(request, 'python.html')


@login_required
def java_test(request):
    return render(request, 'java.html')


@login_required
def eyc_test(request):
    return render(request, 'eyc.html')
