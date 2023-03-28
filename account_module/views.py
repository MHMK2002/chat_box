from django.conf import settings
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.views import View

from account_module.forms import SignUpForm, ProfileForm, ChangePasswordForm, ResetPasswordForm
from account_module.models import User
from mail.main import send_activation_email, send_password_reset_email


# Create your views here.
class LoginView(View):
    def get(self, request):
        send_mail(subject='Activate your account', message='Activate your account',
                  from_email=settings.EMAIL_BACKEND, recipient_list=['khanihasan1381@gmail.com'])
        user = request.user
        if user.is_authenticated:
            return redirect('home')
        return render(request, 'account_module/login.html')

    def post(self, request: HttpRequest):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            context = {
                'errors': 'Username or password is incorrect'
            }
            return render(request, 'account_module/login.html', context)
        if user.is_active is False:
            context = {
                'errors': 'Your account is not active'
            }
            return render(request, 'account_module/login.html', context)
        login(request, user)
        return redirect('home')


class SignUpView(View):
    def get(self, request: HttpRequest):
        user = request.user
        if user.is_authenticated:
            pass
            return redirect('home')

        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'account_module/signup.html', context)

    def post(self, request: HttpRequest):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'account_module/signup.html', context)
        user = form.save()
        send_activation_email(user)
        return redirect('login')


class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        form = ChangePasswordForm(user.id)
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'account_module/change-password.html', context)

    def post(self, request: HttpRequest):
        user = request.user
        form = ChangePasswordForm(id=user.id, data=request.POST)
        if not form.is_valid():
            context = {
                'user': user,
                'form': form
            }
            return render(request, 'account_module/change-password.html', context)
        user.set_password(form.cleaned_data.get('new_password'))
        user.save()
        logout(request)
        return redirect('login')


class ActivateAccountView(View):
    def get(self, request: HttpRequest, code):
        user = User.objects.filter(email_activation_code=code).first()
        if user is None:
            return redirect('login')
        return render(request, 'account_module/activate-account.html')

    def post(self, request: HttpRequest, code):
        user = User.objects.filter(email_activation_code=code).first()
        if user is None:
            raise Http404('Page not found')
        user.is_active = True
        user.set_email_activation_code()
        user.save()
        return render(request, 'account_module/success.html', {
            'message': 'Your account is activated'
        })


def logout_view(request):
    logout(request)
    return render(request, 'account_module/logout.html')


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        return render(request, 'account_module/forget-password.html')

    def post(self, request: HttpRequest):
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            context = {
                'errors': 'Email not found'
            }
            return render(request, 'account_module/forget-password.html', context)
        send_password_reset_email(user)
        return render(request, 'account_module/success.html', {
            'message': 'Password reset email sent'
        })


class ResetPasswordView(View):
    def get(self, request: HttpRequest, code):
        user = User.objects.filter(password_reset_code=code).first()
        if user is None:
            return redirect('login')
        form = ResetPasswordForm()
        return render(request, 'account_module/reset-password.html', {
            'form': form
        })

    def post(self, request: HttpRequest, code):
        save = request.POST['save']
        if save is None:
            return redirect('login')
        user = User.objects.filter(password_reset_code=code).first()
        if user is None:
            raise Http404('Page not found')
        form = ResetPasswordForm(request.POST)
        if not form.is_valid():
            return render(request, 'account_module/reset-password.html', {
                'form': form
            })
        user.set_password(form.cleaned_data.get('password'))
        user.set_email_activation_code()
        user.save()
        return render(request, 'account_module/success.html', {
            'message': 'Your password is reset'
        })
