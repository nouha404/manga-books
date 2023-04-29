from django.urls import path
from .views import InscriptionView, CollectionList, StatiticView, CollectionDetails, CollectionUpdate, CollectionDelete

urlpatterns = [
    path('', InscriptionView.as_view(), name='inscription'),
    path('acceuil/', CollectionList.as_view(), name='base'),
    path('stat/', StatiticView.as_view(), name='stat'),
    path('details/<slug:slug>/', CollectionDetails.as_view(), name='details'),
    path('details/<slug:slug>/editer/', CollectionUpdate.as_view(), name='editer'),
    path('details/<slug:slug>/delete/', CollectionDelete.as_view(), name='deleted')
]
