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

# View User Profile
def view_user(request, pk):
    user = get_list_or_404(UserProfile, id=pk)
    return render(request, 'view_user.html', {'user': user})

# Update User Profile
def update_user(request, pk):
    user = get_list_or_404(UserProfile, id=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = UserProfileForm(instance=user)
        return render(request, 'update_user.html', {'form': form})
    
# Delete User Profile
def delete_user(request, pk):
    user = get_list_or_404(UserProfile, id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard')
    return render(request, 'delete_user.html', {'user': user})