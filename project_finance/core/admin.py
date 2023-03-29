from django.contrib import admin
from .models import Deposit, Category, Operation, CategoryType


admin.site.register((Deposit, Category, Operation, CategoryType))
