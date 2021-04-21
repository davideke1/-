from django.shortcuts import render


def home(request):
    return render(request, "crud_blog/index.html")
