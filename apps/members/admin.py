from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'role',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Member, MemberAdmin)
