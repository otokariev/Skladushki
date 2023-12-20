from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),

    path('api/account/', AccountAPIList.as_view(), name='account'),
    path('api/account/<int:pk>/', AccountAPIUpdate.as_view(), name='account_id'),
    # path('api/user_delete/<int:pk>/', UserModel.as_view(), name='user_delete'),

    path('api/about/', AboutAPIView.as_view(), name='about'),
    path('api/contacts/', ContactsAPIView.as_view(), name='contacts'),

    path('api/auth/', include('rest_framework.urls')),

    # path('api/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
