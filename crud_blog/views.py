from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm, CommentForm, ArticleForm,\
    UpdateArticleForm
from django.contrib.auth import authenticate, login, logout
from .models import Article, Comment
import datetime

date = datetime.datetime.now()

def home(request):
    articles = Article.objects.all().order_by("-timestamp")[:3]

    context = {
        "articles": articles
    }
    return render(request, "crud_blog/index.html", context)


def create_article(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            content = form.cleaned_data.get("content")

            article = Article(
                user=user, title=title, 
                timestamp = date,
                image=image, content=content
            )
            article.save()
            return redirect("blog:home")
        return redirect("blog:create")

    context = {
        "form": form
    }
    return render(request, "crud_blog/create-article.html", context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("message")

            comment = Comment(
                user = request.user,
                message = message,
                article = article
            )
            comment.save()

    context = {
        "article": article,
        "form": form,
        "comments": comments
    }
    return render(request, "crud_blog/blog-single.html", context)


def update_article(request, pk):
    article = Article.objects.get(id=pk)
    form = UpdateArticleForm(instance=article)

    if request.method == "POST":
        form = UpdateArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
        return redirect("blog:update")

    context = {
        "article": article,
        "form": form
    }
    return render(request, "crud_blog/update-article.html", context)


def confirm_delete_article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "crud_blog/confirm-delete-article.html", {"article": article})


def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect("blog:home")

def register_page(request):
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


def login_page(request):
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
            if user is not None:
                login(request, user)
                return redirect("blog:home")
        return redirect("blog:login")

    context = {
        "form": form
    }
    return render(request, "crud_blog/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("blog:home")


def about(request):
    return render(request, "crud_blog/about.html")