from django.db import models



class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(default="No description provided")
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

class Order(models.Model):
    order_number = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

# Create your models here.
