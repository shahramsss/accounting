from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, null=True, blank=True)
    price = models.DecimalField(max_digits=12 , decimal_places=0)


class Repository(models.Model):
    title = models.CharField(max_length=128)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)


class sell(models.Model):
    pass


class buy(models.Model):
    pass
