from django.shortcuts import render
from django.views.generic import TemplateView

from conversation_module.models import Conversation


# Create your views here.
class ConversationView(TemplateView):
    template_name = 'conversation_module/conversation.html'

    def get_context_data(self, **kwargs):
        context = super(ConversationView, self).get_context_data(**kwargs)
        context['conversation'] = Conversation.objects.fillter(id=kwargs['conversation_id'])
        user = self.request.user
        context['user'] = user
        return context
