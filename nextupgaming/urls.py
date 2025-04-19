from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # if you created a custom signup view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('accounts/signup/', user_views.signup_view, name='signup'),  # Your custom signup
    path('shop/', include('shop.urls')),
]
