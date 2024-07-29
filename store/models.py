from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=-8, decimal_places=2, max_digits=6)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True)
    image = models.ImageField(upload_to='uploads/product/')


    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=-1)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product