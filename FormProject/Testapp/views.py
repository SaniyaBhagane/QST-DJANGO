from django.shortcuts import render
from Testapp.Forms import StudentForm

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
