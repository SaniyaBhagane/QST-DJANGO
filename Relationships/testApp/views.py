from django.shortcuts import render, redirect
from .models import Person, AadharCard, Father, Children

# Create your views here.
def person_list(request):
    person_list = Person.objects.all()
    return render(request, 'person_list.html', {'person_list': person_list})

def add_person(request):
    if request.method == 'POST':
        name = request.Post.get('name')
        age = request.Post.get('age')
        Person.objects.create(name=name, age=age)
        return redirect('person_list')
    return render(request, 'add_person.html')

def aadhar_list(request):
    aadhars = AadharCard.objects.all()
    return render(request, 'aadhar_list.html', {'aadhars': aadhars})


def add_aadhar(request):
    persons = Person.objects.all()
    if request.method == 'POST':
        person_id = request.POST.get('person')
        number = request.POST.get('number')
        person = Person.objects.get(id=person_id)
        AadharCard.objects.create(person=person, number=number)
        return redirect('aadhar_list')
    return render(request, 'add_aadhar.html', {'persons': persons})


def father_list(request):
    fathers = Father.objects.all()
    return render(request, 'father_list.html', {'fathers': fathers})


def add_father(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Father.objects.create(name=name, age=age)
        return redirect('father_list')
    return render(request, 'add_father.html')


def children_list(request):
    children = Children.objects.all()
    return render(request, 'children_list.html', {'children': children})

def add_child(request):
    fathers = Father.objects.all()
    if request.method == 'POST':
        father_id = request.POST.get('father')
        name = request.POST.get('name')
        father = Father.objects.get(id=father_id)
        Children.objects.create(father=father, name=name)
        return redirect('children_list')
    return render(request, 'add_child.html', {'fathers': fathers})
