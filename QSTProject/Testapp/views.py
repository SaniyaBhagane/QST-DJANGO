from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def template_view(request):
    name = 'hritik'
    marks = 100
    rollno = 111
    my_dic = {'uname':name,'umarks':marks,'uroll':rollno}
    return render(request,'home.html',context=my_dic)
    

def about(request):
    return render(request,"about.html")