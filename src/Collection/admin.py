from django.contrib import admin

# Register your models here.
from .models import MangaWiki


@admin.register(MangaWiki)
class MangaWikiAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'author',
        'number_of_volume',
        'status',
        'description'
    )
