from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'petstoadopt/',
        view = views.PetsToAdoptView.as_view(),
        name = 'url_petstoadopt'
    ),
    path(
        route = 'petsadopted/',
        view = views.PetsAdopted.as_view(),
        name = 'url_petsadopted'
    ),
]
