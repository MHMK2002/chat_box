from django.urls import path

from profile_module import views

urlpatterns = [
    path('', views.Profile.as_view(), name='tabpane_profile'),

    path('status/<str:status>', views.set_status, name='set_status'),

    path('update/personal-form', views.PersonalInfo.as_view(), name='personal_form'),
    path('update', views.Settings.as_view(), name='tabpane_settings'),
    path('update/avatar', views.save_avatar, name='save_avatar'),
]
