from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """docstring for Article."""
    title = models.CharField(max_length=120)
    content = models.TextField()