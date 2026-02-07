from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'
    
class AadharCard(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    number = models.CharField(max_length=12)
    
class Father(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'

class Children(models.Model):
    father = models.ForeignKey(Father, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'
