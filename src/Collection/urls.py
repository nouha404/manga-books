from django.urls import path
from .views import CollectionView

urlpatterns = [
    path('', CollectionView.as_view(), name='add-collection')
]
