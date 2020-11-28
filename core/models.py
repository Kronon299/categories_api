from django.db import models


class Category(models.Model):
    parentCategory = models.ForeignKey('self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)