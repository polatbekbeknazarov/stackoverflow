from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from tinymce.models import HTMLField


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    body = HTMLField(blank=False)
    tag = models.ManyToManyField(Tag, blank=False)
    closed = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
