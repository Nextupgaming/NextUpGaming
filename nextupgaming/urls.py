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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),    # Login, logout, password reset
]
