from django.db import models


class CategoryType(models.Model):
    type = models.CharField(primary_key=True, null=False)


class Category(models.Model):
    name = models.CharField(primary_key=True)
    type = models.ForeignKey('CategoryType', on_delete=models.PROTECT, null=False)


class Deposit(models.Model):
    name = models.CharField(primary_key=True)
    balance = models.IntegerField()