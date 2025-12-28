from django.shortcuts import render, redirect, get_list_or_404
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def dashboard(request):
    profiles = UserProfile.objects.all()
    return render(request, 'dashboard.html', {'profiles': profiles})