from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import (
    Event,
    EventPhoto,
)

class AllEventsView(ListView):
    model = Event
    queryset = Event.objects.all().filter(status = True)
    template_name = "event/all_events.html"
    context_object_name = "context_allevents"

class EventDetailView(ListView):
    model = Event
    template_name = "event/event.html"
    context_object_name = "context_eventdetail"

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        queryset = self.model.objects.all()
        return queryset.filter(id = pk)

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)

        # EventPhoto context
        query_eventphotos = EventPhoto.objects.filter(status = True, event__pk = pk).select_related()
        context['context_eventphotos'] = query_eventphotos

        return context
