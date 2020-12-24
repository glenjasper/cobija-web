from django.db import models
from auditlog.registry import auditlog

class Role(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    order = models.SmallIntegerField(verbose_name = 'Order', default = 0)
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_role"
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

class TypePet(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_typepet"
        verbose_name = "Type of pet"
        verbose_name_plural = "Types of pet"
        ordering = ["name"]

    def __str__(self):
        return self.name

class PetSize(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_petsize"
        verbose_name = "Pet size"
        verbose_name_plural = "Pet size"
        ordering = ["name"]

    def __str__(self):
        return self.name

class PetColor(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_petcolor"
        verbose_name = "Pet color"
        verbose_name_plural = "Pet color"
        ordering = ["name"]

    def __str__(self):
        return self.name

class TypePartner(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_typepartner"
        verbose_name = "Type of partner"
        verbose_name_plural = "Types of partner"
        ordering = ["name"]

    def __str__(self):
        return self.name

auditlog.register(Role)
auditlog.register(TypePet)
auditlog.register(PetSize)
auditlog.register(PetColor)
auditlog.register(TypePartner)
