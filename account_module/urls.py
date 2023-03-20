from account_module import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]
