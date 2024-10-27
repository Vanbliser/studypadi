"""contains utility celery task function"""

from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from django.conf import settings
from django.core.mail import EmailMessage
import pyotp
from .models import User
from celery import shared_task


MAX_ATTEMPT = int(getattr(settings, 'MAX_ATTEMPT', 3))
TIMEOUT = int(getattr(settings, 'TIMEOUT', 300))
DIGITS = int(getattr(settings, 'DIGITS', 6))
FROM_EMAIL = getattr(settings, 'EMAIL_HOST_USER')


def generate_otp(email):
    """Generate time-based OTP"""

    secret = pyotp.random_base32()
    otp = pyotp.TOTP(secret, interval=TIMEOUT, digits=DIGITS)
    cache.set(f"otp-{email}", otp.now(), timeout=TIMEOUT)
    cache.set(f"secret-{email}", secret, timeout=TIMEOUT)
    cache.set(f"attempt-{email}", 0, timeout=TIMEOUT)
    return otp.now()

def verify_otp(otp, email):
    """Verify the OTP"""

    otp = cache.get(f"otp-{email}")
    attempts = cache.get(f"attempt-{email}")
    secret = cache.get(f"secret-{email}")
    if otp and secret:
        # Check attempts
        if attempts > MAX_ATTEMPT:
            raise ValueError(_(f"Too many attempts. Please try again later."))
        totp = pyotp.TOTP(secret, interval=TIMEOUT, digits=int(DIGITS))
        return totp.verify(otp)
    return False

@shared_task()
def send_otp(otp, email):
    user = User.objects.get(email=email)
    subject = "One Time Password"
    body = f"hi {user.first_name}, your OTP is {otp}"
    email = EmailMessage(subject=subject, body=body, to=[user.email], from_email=FROM_EMAIL)
    email.send(fail_silently=True)
