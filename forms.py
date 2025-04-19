
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PLATFORM_CHOICES = [
    ('PSN', 'PlayStation'),
    ('XBOX', 'Xbox'),
    ('PC', 'PC'),
]

class SignUpForm(UserCreationForm):
    gamertag = forms.CharField(max_length=50)
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gamertag', 'platform', 'date_of_birth')
