from django.contrib import admin

from .models import SubjedditModel

class SubjedditModelAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(SubjedditModel, SubjedditModelAdmin)