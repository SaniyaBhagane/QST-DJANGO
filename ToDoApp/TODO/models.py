from django.db import models

# todoapp1234
# Create your models here.
class todo(models.Model):
        taskName = models.CharField(max_length= 100)
        dateTime = models.DateTimeField(auto_now_add= True)
        
    
    