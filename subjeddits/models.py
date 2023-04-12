from django.db import models
import datetime
from django.urls import reverse

class Subjeddit(models.Model):
    title = models.CharField(max_length=21)
    creation_date = models.DateTimeField('Created', default=datetime.datetime.now)
    # this makes it look better in Subjeddit.objects.all() and in automatically created admin stuff
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("index", kwargs={"slug": self.slug})
   
#little change
#this is main
