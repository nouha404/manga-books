from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, TemplateView
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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'compte/profile.html'

