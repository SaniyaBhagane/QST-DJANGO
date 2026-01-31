from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def page_count(request):
    count = request.session.get('count', 0)
    newCount = count + 1
    request.session['count'] = newCount
    return render(request, 'count.html', {'count': newCount})

def home(request):
    return render(request, 'home.html')

def show_mobile(request):
    mobiles = request.session.get('mobiles', [])
    return render(request, 'show.html', {'mobiles': mobiles})


def add_mobile(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact_no = form.cleaned_data['contact_no']
            mobiles = request.session.get('mobiles', [])
            mobiles.append({
                'name': name,
                'contact': contact_no
            })
            request.session['mobiles'] = mobiles
    else:
        form = ContactForm()
    return render(request, 'add.html', {'form': form})

def delete_mobile(request, index):
    mobiles = request.session.get('mobiles', [])
    if index < len(mobiles):
        mobiles.pop(index)
        request.session['mobiles'] = mobiles
    return redirect('show')
