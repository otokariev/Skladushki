from django.urls import path
from .views import (
    registration_view,
    ObtainAuthTokenView,
    account_properties_view,
    update_account_view,
    does_account_exist_view,
    ChangePasswordView,
)

urlpatterns = [
    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('profile/', account_properties_view, name="profile"),
    path('profile/update/', update_account_view, name="update"),
    path('login/', ObtainAuthTokenView.as_view(), name="login"),
    path('register/', registration_view, name="register"),
]
