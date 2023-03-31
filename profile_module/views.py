import os
import imghdr
from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from conversation_module.models import Conversation
from private_chat_module.models import PrivateChat
from profile_module.forms import PersonalInfoForm
import base64


# Create your views here.
def set_status(request):
    user: User = request.user
    if not user.is_authenticated:
        raise Http404('User is not authenticated')

    status = request.POST.get('status')
    if status is None or (status != 'active' and status != 'away' and status != 'do not disturb'):
        return HttpResponse(status=400, content='Status is not valid')

    user.profile.status = status
    user.profile.save()
    return HttpResponse(status=200, content='Status updated successfully')


class Profile(View):
    def get(self, request: HttpRequest):
        uesr: User = request.user
        if not uesr.is_authenticated:
            raise Http404('User is not authenticated')
        context = {
            'user': uesr,
        }
        return render(request, 'profile_module/profile.html', context)

    def post(self, request: HttpRequest):
        pass


class Settings(View):
    def get(self, request: HttpRequest):
        user: User = request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        form = PersonalInfoForm(user.id)
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'profile_module/settings.html', context)

    def post(self, request: HttpRequest):
        form = PersonalInfoForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, content='Personal info updated successfully')
        return HttpResponse(status=400, content='Personal info is not valid')


class Contacts(TemplateView):
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


class Calls(View):
    def get(self, request: HttpRequest):
        return render(request, 'profile_module/calls.html')

    def post(self, request: HttpRequest):
        pass


class Chats(View):
    def get(self, request: HttpRequest):
        user: User = request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        channels = user.channel_set.all()
        private_chats = user.privatechat_set.all()
        context = {
            'user': user,
            'channels': channels,
            'private_chats': private_chats,
        }
        return render(request, 'profile_module/chats.html', context)

    def post(self, request: HttpRequest):
        pass


class Bookmark(View):
    def get(self, request: HttpRequest):
        return render(request, 'profile_module/bookmark.html')

    def post(self, request: HttpRequest):
        pass


def save_avatar(request):
    user: User = request.user
    if user.is_authenticated:
        avatar = request.FILES.get('avatar')
        if avatar is None:
            print(request.POST)
            print(request.POST.get('avatar'))
            raise Http404('Avatar is not provided')
        user.profile.avatar = avatar
        user.save()

        return HttpResponse(status=200, content='Avatar saved successfully')
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


class ChatPageView(TemplateView):
    template_name = 'profile_module/chat-partials/chat-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: User = self.request.user
        if not user.is_authenticated:
            raise Http404('User is not authenticated')
        context['user'] = user

        conversation = Conversation.objects.get(id=self.kwargs['conversation_id'])
        context['conversation'] = conversation

        name = ''
        avatar = ''
        about = ''
        status = ''

        if PrivateChat.objects.filter(conversation=conversation).exists():
            chat = PrivateChat.objects.get(conversation=conversation)
            name = chat.get_name(self, user)
            avatar = chat.get_avatar(self, user)
            about = chat.get_about(self, user)
            status = chat.get_status(self, user)
        else:
            chat = conversation.channel
            name = chat.name
            avatar = chat.avatar
            about = chat.about
            status = f'{chat.members.all().count()} Members'

        context['chat_name'] = name
        context['chat_avatar'] = avatar
        context['chat_about'] = about
        context['chat_status'] = status

        return context
