from django.shortcuts import render
from django.views.generic import ListView

from apps.members.models import Member
from apps.about.models import About
from django.db.models import Q
from pprint import pprint

class HomeView(ListView):
    template_name = "core/home.html"
    context_object_name = 'context_members'

    # Two conditions:
    # AND: ~Q(...) & ~Q(...)
    # OR:  ~Q(...) | ~Q(...)
    def get_queryset(self):
        _members_all = Member.objects.all().filter(status = True).order_by('role__order', 'first_name')

        members_all = {}
        group = {}
        n_group = 4
        index_g = 0
        for index, member in enumerate(_members_all, start = 1):
            group.update({index: member})

            if index % n_group == 0:
                members_all.update({index_g: group})
                group = {}
                index_g += 1
        
        if group:
            members_all.update({index_g: group})

        return members_all

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # About context
        query_about = About.objects.get(status = True, pk = 1)
        context['context_about'] = query_about

        return context
