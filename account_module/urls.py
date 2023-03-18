from account_module import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('change-avatar', views.change_avatar, name='change_avatar'),
]
