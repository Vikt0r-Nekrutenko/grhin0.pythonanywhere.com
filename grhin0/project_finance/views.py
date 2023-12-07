from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class DepositAPIViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class OperationAPIViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DebtAPIViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


def main_page_view(request):
    objects_count = Category.objects.count()
    operations_count = Operation.objects.count()

    try:
        str_date = str(Operation.objects.first().date)
        date = datetime.strptime(str_date, '%Y-%m-%d').date()
        month_count = int((datetime.now().date() - date).days)
    except:
        month_count = 0

    return render(request, 'index.html', {
        'objects_count': objects_count,
        'operations_count': operations_count,
        'month_count': month_count,
    })
