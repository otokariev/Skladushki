"""
URL configuration for skladushki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from members.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),

    path('api/v1/members/', UserAPIList.as_view(), name='users'),
    path('api/v1/members/<int:pk>/', UserAPIUpdate.as_view(), name='user_id'),
    # path('api/v1/members_delete/<int:pk>/', UserModel.as_view(), name='members_delete'),

    path('api/v1/about/', AboutView.as_view(), name='about'),
    path('api/v1/contacts/', ContactsView.as_view(), name='contacts'),

    path('api/v1/authorisation/', include('rest_framework.urls')),

    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
