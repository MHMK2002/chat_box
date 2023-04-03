from django.shortcuts import render
from django.views.generic import TemplateView

from message_module.models import Message


# Create your views here.
class MessageView(TemplateView):
    template_name = 'message_module/message.html'

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['message']: Message = Message.objects.filter(id=kwargs['message_id']).first()
        user = self.request.user
        context['user'] = user
        return context
