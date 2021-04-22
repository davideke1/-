from django.urls import path
from .views import home, article, about, register, login, reset_password

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('article/', article, name="article"),
    path('about/', about, name="about"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('reset-password/', reset_password, name="reset-password")
]
