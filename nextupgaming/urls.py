from nextupgaming.views import signup_view
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from nextupgaming import views

path('accounts/signup/', signup_view, name='signup'),

def home(request):
    return HttpResponse("✅ NextUpGaming is LIVE!")

urlpatterns = [
    path('accounts/signup/', signup_view, name='signup'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
]

from django.contrib import admin
from django.urls import path, include
from nextupgaming.views import signup_view  # 👈 ADD THIS

from nextupgaming.views import signup_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),  # 👈 ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup_view, name='signup'),  # 👈 ADD THIS
    path('accounts/', include('django.contrib.auth.urls')),
]
