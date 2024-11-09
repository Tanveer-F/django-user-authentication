from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'registration/home.html')

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user) # Get related profile
    return render(request, 'registration/profile.html', {'user': request.user, 'profile': user_profile})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #dictionary key.
            messages.success(request, f'Account Created for {username}! Now You Can Login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})   
