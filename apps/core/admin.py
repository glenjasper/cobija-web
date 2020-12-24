from django.contrib import admin
from .models import (
    Role,
    TypePet,
    PetSize,
    PetColor,
    TypePartner,
    )

class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class TypePetAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class PetSizeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class PetColorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

class TypePartnerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
    ]
    readonly_fields = ['created', 'updated']

admin.site.register(Role, RoleAdmin)
admin.site.register(TypePet, TypePetAdmin)
admin.site.register(PetSize, PetSizeAdmin)
admin.site.register(PetColor, PetColorAdmin)
admin.site.register(TypePartner, TypePartnerAdmin)
