from django.db import models
from auditlog.registry import auditlog

class Event(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    location = models.CharField(max_length = 250, verbose_name = 'Location', help_text = 'Place of the event')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description of the event')
    link = models.URLField(max_length = 150, blank = True, verbose_name = 'Event link')
    date = models.DateField(verbose_name = 'Date', help_text = 'Date of the event')
    logo = models.ImageField(upload_to = 'events', verbose_name = 'Logo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_event"
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-date"]

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(to = Event, on_delete = models.CASCADE, verbose_name = 'Event')
    photo = models.ImageField(upload_to = 'events', verbose_name = 'Photo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_eventphoto"
        verbose_name = "EventPhoto"
        verbose_name_plural = "EventPhotos"
        ordering = ["photo"]

auditlog.register(Event)
auditlog.register(EventPhoto)
