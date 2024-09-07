from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Includes your accounts app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Includes built-in auth URLs (like login, password reset)
    path('logout/', LogoutView.as_view(), name='logout'),  # Add the logout URL here
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Home page
]
