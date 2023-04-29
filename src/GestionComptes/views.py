from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView, DetailView, UpdateView, DeleteView

from Collection.forms import MangaWikiForm
from Collection.models import MangaWiki
from .forms import Inscription
from .models import CustomUser


class InscriptionView(FormView):
    form_class = Inscription
    template_name = 'compte/inscription.html'
    context_object_name = 'form'
    success_url = reverse_lazy('connexion')

    def form_valid(self, form):
        if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
            context = self.get_context_data(form=form)
            context['errors'] = "Mots de passe non identiques"
            return self.render_to_response(context)

        CustomUser.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        return super().form_valid(form)


class CollectionList(LoginRequiredMixin, ListView):
    model = MangaWiki
    template_name = 'base/items.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = MangaWiki.objects.filter(collection_author=self.request.user)
        print(queryset)
        return MangaWiki.objects.filter(collection_author=self.request.user)


class CollectionDetails(DetailView):
    model = MangaWiki
    template_name = 'base/details.html'
    context_object_name = 'details'


class CollectionUpdate(UpdateView):
    model = MangaWiki
    form_class = MangaWikiForm
    template_name = 'base/update.html'

    # success_url = reverse_lazy('details')

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'slug': self.object.slug})


class CollectionDelete(DeleteView):
    model = MangaWiki
    template_name = 'base/delete.html'
    success_url = reverse_lazy('base')


class StatiticView(ListView):
    model = MangaWiki
    template_name = 'base/statistic.html'
    context_object_name = 'stats'
