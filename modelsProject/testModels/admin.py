from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')
    search_fields = ('first_name', 'last_name')
    list_filter = ('enrollment_date',)

admin.site.register(Student, StudentAdmin)