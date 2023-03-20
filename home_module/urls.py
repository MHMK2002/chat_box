from django.urls import path

from home_module import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
