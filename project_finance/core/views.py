from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Operation
from .serializers import OperationSerializer


class OperationAPIViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
