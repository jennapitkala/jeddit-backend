from django.db import models
import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse

class SubjedditModel(models.Model):
    title = models.CharField(max_length=21)
    creation_date = models.DateTimeField('Created', default=datetime.datetime.now)
    slug = models.SlugField(null=False, unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("index", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
   