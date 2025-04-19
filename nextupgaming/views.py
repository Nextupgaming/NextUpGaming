
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                gamertag=form.cleaned_data['gamertag'],
                platform=form.cleaned_data['platform'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': request.user.userprofile
    })
