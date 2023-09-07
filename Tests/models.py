from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.TextField(max_length=50,null=True)

    def save(self,*args,**kwargs):
        if self.name == "car":
            raise ValueError("Car is not an animal")
        super(Animal,self).save(*args,**kwargs)

    def speak(self):
        return f'The {self.name} says "{self.sound}"'
