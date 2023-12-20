from django.urls import path
from . import views
from account.views import api_detail_account_view

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('search', views.search, name='search'),

    # path('api_detail_account_view/', api_detail_account_view, name='detail'),  #!FIXME change to <slug>/
]
