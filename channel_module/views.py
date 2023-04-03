from django.shortcuts import render
from django.views.generic import TemplateView

from channel_module.models import Channel


# Create your views here.
class ChannelChatView(TemplateView):
    template_name = 'channel_module/chat-page.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelChatView, self).get_context_data(**kwargs)
        conversation = Channel.objects.get(id=kwargs['conversation_id'])
        context['channel'] = Channel.objects.fillter(conversation=conversation).first()
        context['conversation_id'] = conversation.id
        return context
