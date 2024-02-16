from django.db import models

# Create your models here.
from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name

class ProductAtrribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return f'{self.attribute.name} {self.product.name}'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)   
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)    

    class Meta:
        indexes = [
            models.Index(fields=['product'])
        ]