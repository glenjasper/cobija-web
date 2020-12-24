from django.contrib import admin
from .models import (
    Pet,
    PetPhoto
)

class PetPhotoInline(admin.TabularInline):
    model = PetPhoto

    def get_extra(self, request, obj=None, **kwargs):
        extra = 10
        if obj:
            return extra - obj.petphoto_set.count()
        return extra

    '''
    # Número máximo de items a agregar
    def get_max_num(self, request, obj = None, **kwargs):
        max_num = 15
        if obj and obj.parent:
            return max_num - 5
        return max_num
    '''

class PetAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'typepet',
        'petsize',
        'petcolor',
        'adopted',
        'status',
    ]
    readonly_fields = ['created', 'updated']
    inlines = [
        PetPhotoInline,
    ]

admin.site.register(Pet, PetAdmin)
