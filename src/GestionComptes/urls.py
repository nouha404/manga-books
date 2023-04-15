from django.urls import path
from .views import InscriptionView, CollectionList

urlpatterns = [
    path('', InscriptionView.as_view(), name='inscription'),
    path('acceuil/', CollectionList.as_view(), name='base')
]
