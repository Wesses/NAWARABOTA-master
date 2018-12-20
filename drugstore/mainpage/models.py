from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    location = models.CharField(max_length=70)
    picture = models.ImageField
    goods = models.Manager

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name
