from django.shortcuts import render, redirect

def name_view(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        return redirect('age')
    return render(request, 'testapp/name.html')

def age_view(request):
    if request.method == "POST":
        request.session['age'] = request.POST['age']
        return redirect('qualification')
    return render(request, 'testapp/age.html')

def qualification_view(request):
    if request.method == "POST":
        request.session['qualification'] = request.POST['qualification']
        return redirect('result')
    return render(request, 'testapp/qualification.html')

def result_view(request):
    context = {
        'name': request.session.get('name'),
        'age': request.session.get('age'),
        'qualification': request.session.get('qualification'),
    }
    return render(request, 'testapp/result.html', context)
