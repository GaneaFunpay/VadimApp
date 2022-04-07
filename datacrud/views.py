from django.shortcuts import render
from rest_framework import generics

from . import models, serializers


class DataRetrieveView(generics.RetrieveAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.DataSerializer


class DataCreateView(generics.ListCreateAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.DataSerializer


