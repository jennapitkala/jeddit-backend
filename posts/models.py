from django.db import models
from datetime import datetime
from django.urls import reverse

from subjeddits.models import Subjeddit


class Post(models.Model):
    subjeddit = models.ForeignKey(Subjeddit, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=40000)
    creation_date = models.DateTimeField('Created', default=datetime.now)
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("j:comments", kwargs={"slug": self.subjeddit.slug, "comments_slug": self.slug})
    #author will come later
    #comments will come later