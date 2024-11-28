import os
from django.core.mail import send_mail
from django.conf import settings

def send_notification(value):
    subject = "Threshold Alert"
    message = f"The threshold value {value} has been crossed"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [os.getenv('NOTIFICATION_EMAIL')]
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return True
    except Exception as e:
        raise Exception("Failed to send notification") 