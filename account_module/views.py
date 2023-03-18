from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from account_module.forms import SignUpForm
from account_module.models import User


# Create your views here.
class LoginView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            # TODO: Go to dashboard
            pass
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
        # TODO: Dashboard or Chat-list


class SignUpView(View):
    def get(self, request: HttpRequest):
        user = request.user
        if user.is_authenticated:
            # TODO: Go to dashboard
            pass
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
        login(request, user)
        # TODO: Go To Dashboard
