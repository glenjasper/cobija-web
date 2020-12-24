from django.contrib import admin
from .models import Partner

class PartnerAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'type_partner',
        'status',
    ]
    readonly_fields = ['created', 'updated']

    def type_partner(self, obj):
        return ",\n".join([p.name for p in obj.typepartner.all()])

admin.site.register(Partner, PartnerAdmin)
