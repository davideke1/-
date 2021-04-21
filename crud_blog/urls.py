from django.urls import path
from .views import home, article

urlpatterns = [
    path('', home, name="home"),
    path('article/', article, name="article")
]
