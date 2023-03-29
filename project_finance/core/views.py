from django.shortcuts import render
from rest_framework import generics
from .models import Deposit
from .serializers import DepositSerializer


class DepositAPIView(generics.ListAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer