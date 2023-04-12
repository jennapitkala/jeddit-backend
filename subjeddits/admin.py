from django.contrib import admin

from .models import Subjeddit

class SubjedditAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Subjeddit, SubjedditAdmin)