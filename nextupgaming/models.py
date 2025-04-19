from django.db import models
from django.contrib.auth.models import User
from datetime import date

PLATFORM_CHOICES = [
    ('PSN', 'PlayStation'),
    ('XBOX', 'Xbox'),
    ('PC', 'PC'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    gamertag = models.CharField(max_length=50)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    date_of_birth = models.DateField()

    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    @property
    def age(self):
        return self.calculate_age()

    def __str__(self):
        return self.gamertag
