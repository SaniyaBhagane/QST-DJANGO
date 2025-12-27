from django.shortcuts import render
from testApp.forms import StudentForm

# Create your views here.
def from_view(request):
    form = StudentForm()
    return render(request, 'testApp/StudentForm.html', {'form': form})