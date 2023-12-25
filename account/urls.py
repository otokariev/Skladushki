from django.urls import path
from .views import (
    registration_view,
    LoginAuthTokenView,
    account_profile_view,
    update_account_profile_view,
    check_if_account_exists,
    ChangePasswordView,
)

urlpatterns = [
    path('check_if_account_exists/', check_if_account_exists, name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('profile/', account_profile_view, name="profile"),
    path('profile/update/', update_account_profile_view, name="update"),
    path('login/', LoginAuthTokenView.as_view(), name="login"),
    path('register/', registration_view, name="register"),
]
