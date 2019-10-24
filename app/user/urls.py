from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views

from .views import LoginView, LogoutView, SignUpView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),

    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            subject_template_name='registration/password_reset_subject.txt',
            email_template_name='registration/password_reset_email.html'),
        name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset/complete', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_complete.html'),
        name='password_reset_complete')

]