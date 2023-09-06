from django.db import models
from account.models import Account, Customer

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
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    mproduct = models.ForeignKey(MilkProduct, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        if(self.product.price!=None):
            return self.quantity * self.product.price
        else:
            return self.quantity * self.mproduct.price    

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mproduct = models.ForeignKey(MilkProduct, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        if(self.product.price!=None):
            return self.quantity * self.product.price
        else:
            return self.quantity * self.mproduct.price
        
class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mproduct = models.ForeignKey(MilkProduct, on_delete=models.CASCADE, blank=True, null=True)