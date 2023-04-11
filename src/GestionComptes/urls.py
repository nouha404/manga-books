from django.urls import path, include
from .views import InscriptionView, ProfileView

urlpatterns = [
    path('', InscriptionView.as_view(), name='inscription'),
    path('acceuil/', ProfileView.as_view(), name='base')
]
