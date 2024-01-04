from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import user_profile, user_register, edit_user

urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/',LoginView.as_view(), name='login'),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("profile/", user_profile, name="user_profile"),
    path("sign_up/",user_register, name="user_register"),
    # path("sign_up/", SignUpView.as_view(), name="user_register")
    path("profile/edit/", edit_user, name="edit_user_information")
]