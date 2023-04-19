from django.db import models
from datetime import datetime
from django.urls import reverse

from posts.models import PostModel


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    creation_date = models.DateTimeField('Created', default=datetime.now)
    
    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse("j:comments", kwargs={"slug": PostModel.subjeddit.slug, "comments_slug": PostModel.slug})
    

    #author will come later
