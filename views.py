
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.urls import reverse
from .forms import SignUpForm
from .models import UserProfile
from .tokens import account_activation_token

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            UserProfile.objects.create(
                user=user,
                gamertag=form.cleaned_data['gamertag'],
                platform=form.cleaned_data['platform'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )

            current_site = get_current_site(request)
            mail_subject = 'Activate your NextUpGaming.gg account'
            message = render_to_string('emails/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(mail_subject, message, to=[form.cleaned_data.get('email')])
            email.send()
            return HttpResponse('Please confirm your email address to complete registration.')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': request.user.userprofile
    })
