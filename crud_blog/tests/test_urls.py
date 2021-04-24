from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crud_blog.models import Article, Comment
from crud_blog.views import home, article, about, register_page, login_page,\
    logout_page, update_article, delete_article, create_article, delete_article


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse("blog:home")
        self.assertEquals(resolve(url).func, home)

    def test_article_is_resolves(self):
        url = reverse("blog:article", args=["1"])
        self.assertEquals(resolve(url).func, article)

    def test_about_is_resolves(self):
        url = reverse("blog:about")
        self.assertEquals(resolve(url).func, about)

    def test_register_page_is_resolves(self):
        url = reverse("blog:register")
        self.assertEquals(resolve(url).func, register_page)

    def test_login_page_is_resolves(self):
        url = reverse("blog:login")
        self.assertEquals(resolve(url).func, login_page)
    
    def test_logout_page_is_resolves(self):
        url = reverse("blog:logout")
        self.assertEquals(resolve(url).func, logout_page)

    def test_update_page_is_resolves(self):
        url = reverse("blog:update", args=["1"])
        self.assertEquals(resolve(url).func, update_article)

    def test_create_page_is_resolves(self):
        url = reverse("blog:create")
        self.assertEquals(resolve(url).func, create_article)

    def test_confirm_delete_page_is_resolves(self):
        url = reverse("blog:delete", args=["1"])
        self.assertEquals(resolve(url).func, delete_article)