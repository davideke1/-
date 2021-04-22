from django.shortcuts import render
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "crud_blog/index.html")


def article(request):
    return render(request, "crud_blog/blog-single.html")


def register(request):
    form = UserCreateForm()

    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:login")
        print("Something's not right.")
        return redirect("blog:register")

    context = {
        "form": form
    }
    return render(request, "crud_blog/register.html", context)


def login(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print(form)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request, username=username, password=password
            )
            profile = Profile(
                user = username
            )
            profile.save()
            if user is not None:
                login(request, user)
                return redirect("blog:dashboard")
        return redirect("blog:login")

    context = {
        "form": form
    }
    return render(request, "crud_blog/login.html", context)


def logout_page(request):
    logout(request)


def reset_password(request):
    return render(request, "crud_blog/reset-password.html")


def about(request):
    pass