
from django.contrib import admin
from django.urls import path, include
from .views import signup_view, profile_view, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
