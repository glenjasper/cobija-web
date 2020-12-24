from django.db import models
from auditlog.registry import auditlog
from apps.core.models import (
    TypePet,
    PetSize,
    PetColor,
)

class Pet(models.Model):
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (MAN, 'Male'),
        (WOMAN, 'Female'),
    )
    name = models.CharField(max_length = 50, verbose_name = 'Name')
    sex = models.PositiveIntegerField(choices = SEX_CHOICES, verbose_name = 'Sex')
    aproximated_age = models.CharField(max_length = 50, verbose_name = 'Aproximated age')
    birthdate = models.DateField(blank = True, null = True, verbose_name = 'Birthdate')
    typepet = models.ForeignKey(to = TypePet, on_delete = models.CASCADE, verbose_name = 'Type of pet')
    petsize = models.ForeignKey(to = PetSize, on_delete = models.CASCADE, verbose_name = 'Pet Size')
    petcolor = models.ForeignKey(to = PetColor, on_delete = models.CASCADE, verbose_name = 'Pet Color')
    adopted = models.BooleanField(default = False, verbose_name =  'Adopted')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_pet"
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        # ordering = ["name"]

    def __str__(self):
        return self.name

class PetPhoto(models.Model):
    pet = models.ForeignKey(to = Pet, on_delete = models.CASCADE, verbose_name = 'Pet')
    photo = models.ImageField(upload_to = 'pets', verbose_name = 'Photo', help_text = 'Reference image')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Pet photo"
        verbose_name_plural = "Pet photos"
        ordering = ["photo"]

    # def __str__(self):
    #    return self.photo

auditlog.register(Pet)
auditlog.register(PetPhoto)
