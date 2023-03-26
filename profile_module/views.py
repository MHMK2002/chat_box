import os
import imghdr
from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from profile_module.forms import PersonalInfoForm
import base64


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
            return HttpResponse(status=200, content='Personal info updated successfully')
        return HttpResponse(status=400, content='Personal info is not valid')


class TabpaneContacts(TemplateView):
    template_name = 'profile_module/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: User = self.request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        user_contacts = user.profile.contacts.all()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        contacts = {}
        for letter in alphabet:
            temp = user_contacts.filter(username__istartswith=letter).all()
            if len(temp) > 0:
                contacts[letter] = temp
        context['contacts_list'] = contacts
        return context


def save_avatar(request):
    user = request.user
    if user.is_authenticated:
        if request.POST.get('avatar') is None:
            print(request.POST.get('avatar'))
            raise Http404('Avatar is not provided')
        avatar = request.POST.get('avatar')
        # convert base64 to image
        file = base64.b64decode(avatar)
        extension = imghdr.what(None, file)
        file_name = f'{user.username}.{extension}'
        # save image to media folder
        with open(os.path.join('media', 'user', file_name), 'wb') as f:
            f.write(file)
        user.profile.avatar = str(settings.MEDIA_ROOT) + f'\\user\\{file_name}'
        user.profile.save()
        return HttpResponse('Avatar saved')
    raise Http404('User is not authenticated')


class PersonalInfo(View):
    def get(self, request):
        user = request.user
        form = PersonalInfoForm(user.id)
        if user.is_authenticated:
            context = {
                'form': form,
            }
            return render(request, 'profile_module/personal-form.html', context)
        raise Http404('User is not authenticated')

    def post(self, request):
        form = PersonalInfoForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'profile_module/personal-form.html', {'form': form})
