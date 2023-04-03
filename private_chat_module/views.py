from django.shortcuts import render
from django.views.generic import TemplateView

from private_chat_module.models import PrivateChat


# Create your views here.


class PrivateChatView(TemplateView):
    template_name = 'private_chat_module/chat-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conversation = kwargs['conversation_id']
        user = kwargs['request'].user
        private_chat = PrivateChat.objects.filter(conversation=conversation).first()
        context['user'] = private_chat.get_user(user)
        context['conversation_id'] = conversation.id
        return context
