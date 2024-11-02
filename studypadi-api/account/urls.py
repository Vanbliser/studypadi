from django.urls import path
from .views import RegisterUserView, VerifyOTPView, ResendOTPView, LoginView, TestAuthView, ForgetPasswordView, SetNewPassword, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('signup/', RegisterUserView.as_view(), name='signup'),
  path('verify-otp/', VerifyOTPView.as_view(), name='verify'),
  path('resend-otp/', ResendOTPView.as_view(), name='resend'),
  path('login/', LoginView.as_view(), name='login'),
  path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
  path('forget-password/', ForgetPasswordView.as_view(), name='forget-password'),
  path('reset/', SetNewPassword.as_view(), name='reset'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('test-auth/', TestAuthView.as_view(), name='test-auth'),
]