from django.contrib import admin
from .models import todo

# Register your models here.\

class todolist(admin.ModelAdmin):
    list_display = ('taskName', 'dateTime')

admin.site.register(todo)
