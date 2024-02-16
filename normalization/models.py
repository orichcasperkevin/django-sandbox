from django.db import models



# 1NF each cell in the table must hold a single value, not a set of values
class Product(models.Model):
    name = models.CharField(max_length=100)
    attributes = models.CharField(max_length=500)

class Customer(models.Model):
    name = models.CharField(max_length=100)

# 2NF remove any partial dependecy: when a table has a primary key made up of multiple columns, then all columns in the 
# table should depend on the entire primary key
    
# 3NFremove all transitive dependencies.
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)   
    product_description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    customer_phone_number = models.CharField(max_length=100)

    # class Meta:
    #     indexes = [
    #         models.Index(fields=['product'])
    #     ]