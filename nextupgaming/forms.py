
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

PLATFORM_CHOICES = [
    ('PSN', 'PlayStation'),
    ('XBOX', 'Xbox'),
    ('PC', 'PC'),
]

class SignUpForm(UserCreationForm):
    gamertag = forms.CharField(max_length=50)
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'gamertag', 'platform', 'date_of_birth')
