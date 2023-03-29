from django.shortcuts import render
from rest_framework import generics
from .models import Operation
from .serializers import OperationSerializer


class OperationAPIView(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
