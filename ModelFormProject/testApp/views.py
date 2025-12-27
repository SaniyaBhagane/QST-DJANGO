from django.shortcuts import render, HttpResponseRedirect
from testApp.forms import StudentForm
from testApp.models import Student

# Create your views here.
def from_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
    else:
        form = StudentForm()  
    return render(request, 'StudentForm.html', {'form': form})

def student_list(request):
    stud_list = Student.objects.all()
    return render(request, 'StudentList.html', {'students': stud_list})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'StudentDetail.html', {'student': student})

def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'UpdateStudent.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect('/list/')
    return render(request, 'DeleteStudent.html', {'student': student})
