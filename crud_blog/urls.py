from django.urls import path
from .views import home, article, about, register, login_page, reset_password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from .forms import UserPasswordResetForm, UserPasswordResetConfirmForm


app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('<str:pk>/', article, name="article"),
    path('about/', about, name="about"),
    path('register/', register, name="register"),
    path('login/', login_page, name="login"),
    path('reset-password/', reset_password, name="reset-password"),

    # Password Reset
    path('password-reset/', PasswordResetView.as_view(
        template_name='crud_blog/password/forgotten-password.html',
        subject_template_name='crud_blog/password/password-reset-subject.txt',
        email_template_name='crud_blog/password/password-reset-email.html',
        success_url='/crud_blog/password/password-reset/done/',
        form_class=UserPasswordResetForm,
    ), name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='crud_blog/password/forgotten-password-done.html',
    ), name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='crud_blog/password/password-reset-confirm.html',
            form_class=UserPasswordResetConfirmForm,
        ), name='password_reset_confirm'),

    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='crud_blog/password/password-reset-complete.html'
    ), name='password_reset_complete'),
]
