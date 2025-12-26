from django.db import models

# Create your models here.
# pass for superuser = saniya123qst
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_date = models.DateField()
    enrollment_number = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    
    
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
