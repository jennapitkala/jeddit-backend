from django.contrib import admin

from .models import Post


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Post, ArticleAdmin)
