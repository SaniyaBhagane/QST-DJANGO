from django.contrib import admin
from .models import Person, AadharCard, Father, Children

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    
class AadharCardAdmin(admin.ModelAdmin):
    list_display = ('person', 'number')
    
admin.site.register(Person, PersonAdmin)
admin.site.register(AadharCard, AadharCardAdmin)

class FatherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ('father', 'name')
    
admin.site.register(Father, FatherAdmin)
admin.site.register(Children, ChildrenAdmin)