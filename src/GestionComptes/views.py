from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView

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

        CustomUser.object.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        return super().form_valid(form)


# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'base/base.html'


class CollectionList(LoginRequiredMixin, ListView):
    model = MangaWiki
    template_name = 'base/items.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = MangaWiki.objects.filter(collection_author=self.request.user)
        print(queryset)
        return MangaWiki.objects.filter(collection_author=self.request.user)


class StatiticView(ListView):
    model = MangaWiki
    template_name = 'base/statistic.html'
    context_object_name = 'stats'