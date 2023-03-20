from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from account_module.models import User


# Create your views here.
class HomeView(View):
    def get(self, request: HttpRequest):
        user: User = request.user
        if user.is_authenticated:
            return render(request, 'home_module/home-page.html', {'user': user})
        else:
            # TODO: redirect to error page
            pass
