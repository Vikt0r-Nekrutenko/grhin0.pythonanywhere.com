from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Operation
from .serializers import OperationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class OperationAPIViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['amount']
