from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import Partner
from apps.pet.models import Pet
from pprint import pprint

class PartnerAdopterView_original(ListView):
    model = Partner
    queryset = Partner.objects.all().filter(status = True, typepartner__pk = 1).order_by('first_name', 'last_name')
    template_name = "partner/adopter.html"
    context_object_name = "context_partneradopter"

class PartnerAdopterView(ListView):
    template_name = "partner/adopter.html"
    context_object_name = "context_partneradopter"

    def get_queryset(self):
        qry_partners = Partner.objects.all().filter(status = True, typepartner__pk = 1).order_by('first_name', 'last_name')
        dict_partners = {}
        for index, partner in enumerate(qry_partners, start = 1):
            dict_partners.update({index: {partner.pk: partner}})

        qry_pets = Pet.objects.all().filter(status = True, adopted = True).order_by('name')
        dict_pets = {}
        for pet in qry_pets:
            partner_id = pet.adopter.pk
            if partner_id not in dict_pets:
                dict_pets.update({partner_id: [pet]})
            else:
                current = dict_pets[partner_id].copy()
                current.append(pet)
                dict_pets.update({partner_id: current})

        query_set = {}
        for index, data_partner in dict_partners.items():
            for partner_id, partner in data_partner.items():
                query_set.update({index: {'partner': partner, 'pets': dict_pets[partner_id]}})

        return query_set

class PartnerDonorView(ListView):
    model = Partner
    queryset = Partner.objects.all().filter(status = True, typepartner__pk = 2).order_by('first_name', 'last_name')
    template_name = "partner/donor.html"
    context_object_name = "context_partnerdonor"

class PartnerVoluntaryView(ListView):
    model = Partner
    queryset = Partner.objects.all().filter(status = True, typepartner__pk = 3).order_by('first_name', 'last_name')
    template_name = "partner/voluntary.html"
    context_object_name = "context_partnervoluntary"
