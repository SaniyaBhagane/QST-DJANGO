from django.contrib import admin
from .models import Beer

@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'taste', 'alcohol_content', 'mfg_date')
    list_filter = ('taste',)
    search_fields = ('name',)

