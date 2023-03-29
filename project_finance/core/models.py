from django.db import models


class CategoryType(models.Model):
    type = models.CharField(primary_key=True, null=False)