from django.urls import path

from message_module import views

urlpatterns = [
    path('', views.ChatPageView.as_view(), name='chat_page')
]