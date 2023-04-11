from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView
from .forms import MangaWikiForm
from .models import MangaWiki


class CollectionView(CreateView):
    form_class = MangaWikiForm
    template_name = 'addCollection/add-collection.html'
    context_object_name = 'form'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        form.instance.collection_author = self.request.user
        return super().form_valid(form)