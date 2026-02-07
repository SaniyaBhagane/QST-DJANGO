from django.shortcuts import render

# Create your views here.
def helloView(request):
    print("This is the view Statement")
    return render(request, 'hello.html')