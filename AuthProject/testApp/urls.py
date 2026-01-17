from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def python_test(request):
    return render(request, 'python.html')

def java_test(request):
    return render(request, 'java.html')

def eyc_test(request):
    return render(request, 'eyc.html')
