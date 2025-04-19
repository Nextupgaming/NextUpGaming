from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# SIGNUP VIEW
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # or redirect('profile') if you want to send them there
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# PROFILE VIEW
@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': request.user.userprofile,  # FIXED: now properly assigned
    })
