from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    content = models.CharField(max_length=500)
    short_content = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
