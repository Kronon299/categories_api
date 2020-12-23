from django.db import models


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self', verbose_name='Родитель', blank=True, null=True, on_delete=models.SET_NULL, related_name='children'
    )
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
