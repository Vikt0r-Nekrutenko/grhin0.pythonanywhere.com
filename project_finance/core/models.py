from django.db import models


class CategoryType(models.Model):
    type = models.CharField(max_length=255, primary_key=True, null=False)


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    type = models.ForeignKey('CategoryType', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.name}: {self.type}'


class Deposit(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.balance}'


class Operation(models.Model):
    date = models.DateField()
    deposit = models.ForeignKey('Deposit', on_delete=models.PROTECT, null=False)
    amount = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.date} {self.deposit} {self.amount} {self.category}'