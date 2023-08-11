from django.db import models
from account.models import Account

CATEGORY_CHOICES = (
    ('M','Milk'),
    ('Y','Yougurt'),
    ('O','Milk Products'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    composition = models.TextField(blank=True, null=True)
    prodapp = models.TextField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    images = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class MilkProduct(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='milkproduct')
    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price