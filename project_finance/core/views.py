from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class OperationAPIViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['amount']


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
