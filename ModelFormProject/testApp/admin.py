from django.contrib import admin
from testApp.models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'enrollment_date', 'enrollment_number']

admin.site.register(Student, StudentAdmin)
