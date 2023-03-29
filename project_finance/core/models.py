from django.db import models


class CategoryType(models.Model):
    type = models.CharField(max_length=255, primary_key=True, null=False)


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    type = models.ForeignKey('CategoryType', on_delete=models.PROTECT, null=False)


class Deposit(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    balance = models.IntegerField()


class Operation(models.Model):
    date = models.DateField()
    deposit = models.ForeignKey('Deposit', on_delete=models.PROTECT, null=False)
    amount = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=False)