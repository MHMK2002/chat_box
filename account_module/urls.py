from account_module import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('sign-up', views.SignUpView.as_view(), name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('change-password', views.ChangePasswordView.as_view(), name='change-password'),
]
