from turtle import mode
from django.db import models


class Year(models.Model):
    name = models.IntegerField()    

# Create your models here.
class Student(models.Model):
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)