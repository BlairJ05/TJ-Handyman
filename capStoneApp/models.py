from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        default=1,
    )
    text = models.TextField()
    rating = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

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


class RequestModel(models.Model):
    class RequestStatus(models.TextChoices):
        PENDING = "Pending", "Pending"
        ACCEPTED = "Accepted", "Accepted"
        FINISHED = "Finished", "Finished"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requests", default=1
    )
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()
    filename = models.FileField(upload_to="uploads/", blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=RequestStatus.choices, default=RequestStatus.PENDING
    )

    def __str__(self):
        return self.name
