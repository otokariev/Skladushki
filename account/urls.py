from django.urls import path
from .views import (
    registration_view,
    LoginAuthTokenView,
    account_profile_view,
    account_profile_id_view,
    update_account_profile_view,
    check_if_account_exists,
    ChangePasswordView,
    SearchAPIView,
    AccountListBySex,
)

urlpatterns = [
    path('check_if_account_exists/', check_if_account_exists, name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('profile/', account_profile_view, name="profile"),
    path('profile/<int:profile_id>', account_profile_id_view, name="profile_id"),
    path('profile/update/', update_account_profile_view, name="update"),
    path('login/', LoginAuthTokenView.as_view(), name="login"),
    path('register/', registration_view, name="register"),
    path('search/', SearchAPIView.as_view(), name="search"),
    path('<str:sex_identifier>/', AccountListBySex.as_view(), name='sex_identifier'),
]
