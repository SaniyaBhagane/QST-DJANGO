from django.shortcuts import render
from Testapp.Forms import StudentForm, AdvancedStudentForm

def sfview(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = form.cleaned_data['sid']
            sname = form.cleaned_data['sname']
            sage = form.cleaned_data['sage']

            return render(request, 'testapp/StudentForm.html', {
                'form': form,
                'sid': sid,
                'sname': sname,
                'sage': sage
            })

    return render(request, 'testapp/StudentForm.html', {'form': form})


def myview(request):
    if request.method == 'POST':
        form = AdvancedStudentForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALID:", form.cleaned_data)
    else:
        form = AdvancedStudentForm()

    return render(request, 'testapp/AdvForm.html', {'form': form})
