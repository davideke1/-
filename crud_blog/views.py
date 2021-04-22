from django.shortcuts import render


def home(request):
    return render(request, "crud_blog/index.html")


def article(request):
    return render(request, "crud_blog/blog-single.html")


def register(request):
    pass


def login(request):
    pass


def reset_password(request):
    pass


def about(request):
    pass