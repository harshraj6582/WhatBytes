from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, profile_view
from .views import CustomPasswordResetView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile_view, name="profile"),
    path("login/", auth_views.LoginView.as_view(), name="login"), 
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
      # URL for login
]
