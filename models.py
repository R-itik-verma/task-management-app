from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GoogleOAuthKey(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

    def __str__(self):
        return "Google OAuth Key"
