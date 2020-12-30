from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'partneradopter/',
        view = views.PartnerAdopterView.as_view(),
        name = 'url_partneradopter'
    ),
    path(
        route = 'partnerdonor/',
        view = views.PartnerDonorView.as_view(),
        name = 'url_partnerdonor'
    ),
    path(
        route = 'partnervoluntary/',
        view = views.PartnerVoluntaryView.as_view(),
        name = 'url_partnervoluntary'
    )
]
