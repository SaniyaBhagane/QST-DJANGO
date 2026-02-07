from django.contrib import admin
from .models import Person, AadharCard

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    
class AadharCardAdmin(admin.ModelAdmin):
    list_display = ('person', 'number')
    
admin.site.register(Person, PersonAdmin)
admin.site.register(AadharCard, AadharCardAdmin)