from django.contrib import admin
from .models import (
    Event,
    EventPhoto
)

class EventPhotoInline(admin.TabularInline):
    model = EventPhoto

    def get_extra(self, request, obj=None, **kwargs):
        extra = 10
        if obj:
            return extra - obj.eventphoto_set.count()
        return extra

class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'location',
        'date',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    inlines = [
        EventPhotoInline,
    ]

admin.site.register(Event, EventAdmin)
