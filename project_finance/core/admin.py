from django.contrib import admin
from .models import *


admin.site.register((Deposit, Category, Operation, CategoryType, Debt))
