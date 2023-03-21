from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from account_module.models import User
from profile_module.forms import PersonalInfoForm


# Create your views here.
def set_status(request, status):
    user = request.user
    if user.is_authenticated:
        status = status.lower()
        if status == 'active' or status == 'away' or status == 'do not disturb':
            user.profile.status = status
            user.profile.save()
            return render(request, 'home_module/home-page.html', {'user': user})
    raise Http404('User is not authenticated')


class TabpaneProfile(View):
    def get(self, request: HttpRequest):
        uesr: User = request.user
        if not uesr.is_authenticated:
            raise Http404('User is not authenticated')
        context = {
            'user': uesr,
        }
        return render(request, 'partials/tabpanes/tabpane-profile.html', context)

    def post(self, request: HttpRequest):
        pass


class TabpaneSettings(View):
    def get(self, request: HttpRequest):
        user: User = request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        form = PersonalInfoForm(user.id)
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'partials/tabpanes/tabpane-settings.html', context)

    def post(self, request: HttpRequest):
        form = PersonalInfoForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
        context = {
            'user': request.user,
            'form': form,
        }
        return render(request, 'partials/tabpanes/tabpane-settings.html', context)


class TabpaneContacts(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        alphabet = [chr(i) for i in range(65, 91)]
        contacts = {}
        for alpha in alphabet:
            users = User.objects.filter(username__startswith=alpha)
            if users.exists():
                contacts[alpha] = users
        context = {
            'user': user,
            'contacts': contacts,
        }
        return render(request, 'partials/tabpanes/tabpane-contacts.html', context)


def save_avatar(request):
    user = request.user
    if user.is_authenticated:
        user.profile.avatar = request.POST.get('avatar')
        user.profile.save()
        return HttpResponse('Avatar saved')
    raise Http404('User is not authenticated')
