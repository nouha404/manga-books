from django import forms
from .models import MangaWiki


class MangaWikiForm(forms.ModelForm):
    class Meta:
        model = MangaWiki
        fields = '__all__'
