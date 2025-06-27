from django.urls import path
from allauth.account import views as allauth_views

urlpatterns = [
    path("login/", allauth_views.LoginView.as_view(), name="account_login"),
    path("logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
    path("signup/", allauth_views.SignupView.as_view(), name="account_signup"),
    path("password/reset/", allauth_views.PasswordResetView.as_view(), name="account_reset_password"),
    path("password/reset/done/", allauth_views.PasswordResetDoneView.as_view(), name="account_reset_password_done"),
    path("password/change/", allauth_views.PasswordChangeView.as_view(), name="account_change_password"),
    path("password/change/done/", allauth_views.PasswordChangeDoneView.as_view(), name="account_change_password_done"),
    path("password/reset/key/<uidb36>/<key>/", allauth_views.PasswordResetFromKeyView.as_view(), name="account_reset_password_from_key"),
    path("password/reset/key/done/", allauth_views.PasswordResetFromKeyDoneView.as_view(), name="account_reset_password_from_key_done"),
]
