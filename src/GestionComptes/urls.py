from django.urls import path
from .views import InscriptionView, ProfileView

urlpatterns = [
    path('', InscriptionView.as_view(), name='inscription'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
