from django.test import TestCase, Client
from crud_blog.models import Article
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse("blog:home")
        self.article_url = reverse("blog:article", args=["1"])
        self.about_url = reverse("blog:about")
        self.register_page_url = reverse("blog:register")
        self.login_page_url = reverse("blog:login")
        self.logout_page_url = reverse("blog:logout")
        self.update_article_url = reverse("blog:update", args=["1"])
        self.delete_article_url = reverse("blog:delete", args=["1"])
        self.create_article_url = reverse("blog:create")

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/index.html")

    def test_article_GET(self):
        response = self.client.get(self.article_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/blog-single.html")

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/about.html")

    def test_register_page_GET(self):
        response = self.client.get(self.register_page_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/register.html")

    def test_login_page_GET(self):
        response = self.client.get(self.login_page_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/login.html")

    def test_logout_page_GET(self):
        response = self.client.get(self.logout_page_url)
        self.assertEquals(response.status_code, 302)

    def test_update_article_GET(self):
        response = self.client.get(self.update_article_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/update-article.html")

    def test_delete_article_GET(self):
        response = self.client.get(self.delete_article_url)
        self.assertEquals(response.status_code, 200)

    def test_create_article_GET(self):
        response = self.client.get(self.create_article_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crud_blog/create-article.html")