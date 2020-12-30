from django.urls import path
from . import views

urlpatterns = [
    path(
        route = 'eventdetail/<int:pk>/',
        view = views.EventDetailView.as_view(),
        name = 'url_eventdetail'
    ),
    path(
        route = 'allevents/',
        view = views.AllEventsView.as_view(),
        name = 'url_allevents'
    ),
]
