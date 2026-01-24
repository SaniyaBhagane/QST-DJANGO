from django.shortcuts import render

# Create your views here.
def countview(request):
    return render(request, 'Count.html')
