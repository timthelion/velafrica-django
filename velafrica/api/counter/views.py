# -*- coding: utf-8 -*-
from rest_framework import permissions
from rest_framework import generics

from velafrica.counter.models import Entry
from velafrica.counter.serializer import EntrySerializer
from velafrica.api.views import DjangoModelPermissionsMixin


class CounterEntryList(DjangoModelPermissionsMixin, generics.ListCreateAPIView):
    """
    Get a list of all counter entries.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ['organisation', 'date']


class CounterEntryDetail(DjangoModelPermissionsMixin, generics.RetrieveUpdateAPIView):
    """
    Get a detail view of a counter entry.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
