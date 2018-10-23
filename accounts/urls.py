from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name="account.home"),
    path('home/', views.home, name="account.home"),
    path('settings/', views.settings, name="account.settings"),
    path('settings/password', views.password, name="account.password"),
]