from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("blog:update", kwargs={"pk": self.pk})

    # def get_delete_url(self):
    #     return reverse("blog:confirm-delete")

    def get_confirm_delete_url(self):
        return reverse("blog:delete", kwargs={"pk": self.id})
    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"

