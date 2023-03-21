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


def header_references(request):
    return render(request, 'partials/header-references.html')


def footer_references(request):
    return render(request, 'partials/footer-references.html')


def switcher(request):
    return render(request, 'partials/switcher.html')