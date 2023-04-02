from rest_framework import serializers
from .models import *


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('name', 'balance')


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ('type',)


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('id', 'date', 'deposit', 'amount', 'category')


class CategorySerializer(serializers.ModelSerializer):
    operations = OperationSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'type', 'operations']