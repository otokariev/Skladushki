from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('register/', views.register),
    path('login/', views.login),
    path('forgot_password/', views.forgot_password),
]
