from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect

# Create your views here.
def student_list(request):
    stud_list = Student.objects.all()
    return render(request, 'student_list.html', {'students': stud_list})

def form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
    