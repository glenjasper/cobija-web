from django.db import models
from auditlog.registry import auditlog
from apps.core.models import (
    TypePartner,
)

class Partner(models.Model):
    MAN = 1
    WOMAN = 2
    SEX_CHOICES = (
        (MAN, 'Male'),
        (WOMAN, 'Female'),
    )
    first_name = models.CharField(max_length = 50, verbose_name = 'First name')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last name')
    sex = models.PositiveIntegerField(choices = SEX_CHOICES, verbose_name = 'Sex')
    birth_date = models.DateField(blank = True, null = True, verbose_name = 'Birthdate')
    email = models.EmailField(max_length = 80, blank = True, verbose_name = 'E-mail')
    phone = models.CharField(max_length = 150, blank = True, verbose_name = 'Phone')
    address = models.CharField(max_length = 250, blank = True, verbose_name = 'Address')
    image = models.ImageField(upload_to = "partners", verbose_name = "Photo", help_text = 'Please, the photo has to be square, e.g. 500x500')
    # typepartner = models.ForeignKey(to = TypePartner, on_delete = models.CASCADE, verbose_name = 'Type of partner')
    typepartner = models.ManyToManyField(to = TypePartner, verbose_name = 'Type of partner')
    facebook = models.URLField(max_length = 150, blank = True, verbose_name = 'Facebook link')
    instagram = models.URLField(max_length = 150, blank = True, verbose_name = 'Instagram link')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        db_table = "cobija_partner"
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        ordering = ["first_name"]

    def __str__(self):
        return "{first_name} {last_name}".format(
                    first_name = self.first_name,
                    last_name = self.last_name
                )

auditlog.register(Partner)
