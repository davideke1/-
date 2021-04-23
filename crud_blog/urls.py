from django.urls import path
from .views import home, article, about, register_page, login_page,\
    logout_page
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from .forms import UserPasswordResetForm, UserPasswordResetConfirmForm


app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>/', article, name="article"),
    path('about/', about, name="about"),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),

    # Password Reset
    path('password-reset/', PasswordResetView.as_view(
        template_name='crud_blog/password/password-reset.html',
        subject_template_name='crud_blog/password/password-reset-subject.txt',
        email_template_name='crud_blog/password/password-reset-email.html',
        success_url = reverse_lazy('blog:password_reset_done'),
        form_class=PasswordResetForm,
    ), name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='crud_blog/password/password-reset-done.html',
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
