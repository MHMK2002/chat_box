from django.conf import settings
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from account_module.forms import SignUpForm, ProfileForm, ChangePasswordForm
from account_module.models import User


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
        send_mail(subject='Activate your account', message='Activate your account',
                  from_email=settings.EMAIL_BACKEND, recipient_list=[user.email])
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


def logout_view(request):
    logout(request)
    return render(request, 'account_module/logout.html')
