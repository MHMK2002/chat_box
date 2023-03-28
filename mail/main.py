from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(subject, message, from_email, recipient_list, template, context):
    html_message = render_to_string(template, {'message': message}, context)
    send_mail(subject=subject, message=message, from_email=from_email,
              recipient_list=recipient_list, html_message=html_message)


def send_activation_email(user):
    subject = 'Activate your account'
    message = 'To activate your account, please click on the link below\n' \
              'If you did not register, please ignore this email'
    from_email = settings.EMAIL_BACKEND
    recipient_list = [user.email]
    template = 'account_module/activation-email.html'
    context = {
        'email_activation_code': user.email_activation_code,
    }
    send_email(subject, message, from_email, recipient_list, template, context)


def send_password_reset_email(user):
    subject = 'Reset your password'
    message = 'To reset your password, please click on the link below\n' \
              'If you did not request a password reset, please ignore this email'
    from_email = settings.EMAIL_BACKEND
    recipient_list = [user.email]
    template = 'account_module/password-reset-email.html'
    context = {
        'password_reset_code': user.email_activation_code,
    }
    send_email(subject, message, from_email, recipient_list, template, context)
