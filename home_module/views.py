from django.http import HttpRequest, Http404
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
    return render(request, 'home_module/partials/header-references.html')


def footer_references(request):
    return render(request, 'home_module/partials/footer-references.html')


def switcher(request):
    return render(request, 'home_module/partials/switcher.html')


def sidebar(request):
    return render(request, 'home_module/partials/sidebar-menu.html')


