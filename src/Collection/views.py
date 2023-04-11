from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from .forms import MangaWikiForm


class CollectionView(FormView):
    form_class = MangaWikiForm
    template_name = 'addCollection/add-collection.html'
    context_object_name = 'form'