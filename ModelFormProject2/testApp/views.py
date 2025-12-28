from django.shortcuts import render, redirect, get_list_or_404
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
# Dashboard
def dashboard(request):
    profiles = UserProfile.objects.all()
    return render(request, 'dashboard.html', {'profiles': profiles})

# Add User Profile
def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm()
    return render(request, 'add_user.html', {'form': form})

# Edit User Profile