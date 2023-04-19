from django.contrib import admin

from .models import CommentModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("content",)
    

admin.site.register(CommentModel, ArticleAdmin)
