from django.db import models

# Create your models here.
# saniya1234

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    skills = models.CharField(max_length=255)
    dob = models.DateField()

    def __str__(self):
        return self.username