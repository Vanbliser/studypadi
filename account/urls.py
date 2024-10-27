from django.urls import path
from .views import RegisterUserView, VerifyOTPView, ResendOTPView, LoginView, TestAuthView


urlpatterns = [
  path('signup/', RegisterUserView.as_view(), name='signup'),
  path('verify-otp/', VerifyOTPView.as_view(), name='verify'),
  path('resend-otp/', ResendOTPView.as_view(), name='resend'),
  path('login/', LoginView.as_view(), name='login'),
  path('dashboard/', TestAuthView.as_view(), name='dashboard'),
]