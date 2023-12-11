from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('categories/<int:categories_id>/', views.categories, name='categories_id'),
    path('categories/<slug:categories_slug>/', views.categories_by_slug, name='categories_slug'),
]
