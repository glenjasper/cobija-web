from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import (
    Pet,
    PetPhoto
)
from pprint import pprint

class PetsToAdoptView(ListView):
    template_name = "pet/to_adopt.html"
    context_object_name = "context_petstoadopt_simple"

    def get_queryset(self):
        _query = PetPhoto.objects.all().filter(pet__adopted = False, pet__status = True).order_by('pet__name')

        dict_one_photo = {}
        for petphoto in _query:
            if petphoto.pet.pk not in dict_one_photo:
                dict_one_photo.update({petphoto.pet.pk: petphoto})

        return dict_one_photo

    def get_context_data(self, **kwargs):
        context = super(PetsToAdoptView, self).get_context_data(**kwargs)

        # Pets Type context
        _query = Pet.objects.all().filter(adopted = False, status = True).order_by('typepet__name')

        dict_typepet = []
        for pet in _query:
            if pet.typepet.name not in dict_typepet:
                dict_typepet.append(pet.typepet.name)
        context['context_typepet'] = dict_typepet

        # All pets photo
        _query = PetPhoto.objects.all().filter(pet__adopted = False, pet__status = True).order_by('pet__name')

        dict_pets = {}
        for petphoto in _query:
            pk = petphoto.pet.pk
            if pk not in dict_pets:
                dict_pets.update({pk: [petphoto]})
            else:
                current = dict_pets[pk].copy()
                current.append(petphoto)
                dict_pets.update({pk: current})
        context['context_petstoadopt'] = dict_pets

        return context

class PetsAdopted(ListView):
    template_name = "pet/adopted.html"
    context_object_name = "context_petsadopted_simple"

    def get_queryset(self):
        _query = PetPhoto.objects.all().filter(pet__adopted = True, pet__status = True).order_by('pet__name', 'pk')

        dict_one_photo = {}
        for petphoto in _query:
            if petphoto.pet.pk not in dict_one_photo:
                dict_one_photo.update({petphoto.pet.pk: petphoto})

        return dict_one_photo

    def get_context_data(self, **kwargs):
        context = super(PetsAdopted, self).get_context_data(**kwargs)

        # Pets Type context
        _query = Pet.objects.all().filter(adopted = True, status = True).order_by('typepet__name')

        dict_typepet = []
        for pet in _query:
            if pet.typepet.name not in dict_typepet:
                dict_typepet.append(pet.typepet.name)
        context['context_typepet'] = dict_typepet

        # All pets photo
        _query = PetPhoto.objects.all().filter(pet__adopted = True, pet__status = True).order_by('pet__name', 'pk')

        dict_pets = {}
        for petphoto in _query:
            pk = petphoto.pet.pk
            if pk not in dict_pets:
                dict_pets.update({pk: [petphoto]})
            else:
                current = dict_pets[pk].copy()
                current.append(petphoto)
                dict_pets.update({pk: current})
        context['context_petsadopted'] = dict_pets

        return context
