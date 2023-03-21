from django.urls import path

from profile_module import views

urlpatterns = [
    path('status/<str:status>', views.set_status, name='set_status'),
    path('tabpane/profile', views.TabpaneProfile.as_view(), name='tabpane_profile'),
    path('tabpane/settings', views.TabpaneSettings.as_view(), name='tabpane_settings'),
    path('save_avatar', views.save_avatar, name='save_avatar')
]
