from django.urls import path
from .views import RegisterUserView, VerifyOTPView, ResendOTPView, LoginView, TestAuthView, ForgetPasswordView, SetNewPassword


urlpatterns = [
  path('signup/', RegisterUserView.as_view(), name='signup'),
  path('verify-otp/', VerifyOTPView.as_view(), name='verify'),
  path('resend-otp/', ResendOTPView.as_view(), name='resend'),
  path('login/', LoginView.as_view(), name='login'),
  path('dashboard/', TestAuthView.as_view(), name='dashboard'),
  path('forget-password/', ForgetPasswordView.as_view(), name='forget-password'),
  path('reset/', SetNewPassword.as_view(), name='reset')
]