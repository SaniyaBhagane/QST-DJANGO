from django.db import models
from django.urls import reverse

# Choices tuple
# cvbproject 
TASTE_CHOICES = (
    ('Sweet', 'Sweet'),
    ('Sour', 'Sour'),
    ('Bitter', 'Bitter'),
    ('Salty', 'Salty'),
    ('Umami', 'Umami'),
)

class Beer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    taste = models.CharField(
        max_length=10,
        choices=TASTE_CHOICES,
        default='Sweet'
    )
    alcohol_content = models.DecimalField(max_digits=4, decimal_places=2)
    mfg_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('list')
