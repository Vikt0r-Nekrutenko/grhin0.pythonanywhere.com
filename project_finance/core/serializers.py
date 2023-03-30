from rest_framework import serializers
from .models import *


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('date', 'deposit', 'amount', 'category')


class CategorySerializer(serializers.ModelSerializer):
    operations = OperationSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'type', 'operations']