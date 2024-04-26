from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"


class CreateCard(models.Model):
    header = models.CharField(max_length=30, null=True)
    before_Pic = models.ImageField(upload_to="capStoneApp/static/project_images")
    after_Pic = models.ImageField(upload_to="capStoneApp/static/project_images")
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    url = models.URLField(max_length=200, null=True, blank=True)


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
