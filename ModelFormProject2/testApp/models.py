from django.db import models

# Create your models here.
# saniya1234

class UserProfile(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    skills = models.CharField(max_length=255)
    dob = models.DateField()

    def __str__(self):
        return self.username