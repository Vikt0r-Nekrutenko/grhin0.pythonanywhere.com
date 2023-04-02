from django.db import models


class CategoryType(models.Model):
    type = models.CharField(max_length=255, primary_key=True, null=False)

    def __str__(self):
        return f'{self.type}'


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    type = models.ForeignKey('CategoryType', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.name} [{self.type}]'


class Deposit(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    balance = models.IntegerField()

    def __str__(self):
        return f'{self.name}: [{self.balance}]'


class Operation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date = models.DateField()
    deposit = models.ForeignKey('Deposit', on_delete=models.CASCADE)
    amount = models.IntegerField()
    category = models.ForeignKey('Category', related_name='operations', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.id} {self.date} {self.deposit} {self.amount} {self.category}'


class Debt(models.Model):
    deposit = models.ForeignKey('Deposit', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.deposit} {self.name} {self.amount}'
