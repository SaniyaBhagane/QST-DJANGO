from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile


# ---------------- DASHBOARD ----------------
def dashboard(request):
    profiles = UserProfile.objects.all()
    return render(request, 'dashboard.html', {
        'profiles': profiles
    })


# ---------------- ADD USER ----------------
def add_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm()

    return render(request, 'add_user.html', {
        'form': form
    })


# ---------------- VIEW USER ----------------
def view_user(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'view_user.html', {
        'profile': profile
    })


# ---------------- UPDATE USER ----------------
def update_user(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'update_user.html', {
        'form': form,
        'profile': profile
    })


# ---------------- DELETE USER ----------------
def delete_user(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':
        profile.delete()
        return redirect('dashboard')

    return render(request, 'delete_user.html', {
        'profile': profile
    })
