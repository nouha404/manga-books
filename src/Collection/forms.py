from django import forms
from django.urls import reverse

from .models import MangaWiki, Gender


class MangaWikiForm(forms.ModelForm):
    class Meta:
        model = MangaWiki
        fields = (
            'author',
            'number_of_volume',
            'status',
            'note',
            'gender',
            'title',
            'description'
        )
