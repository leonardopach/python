from contact import models
from django.contrib import admin

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_editable = 'show',
    list_per_page = 50
    list_display_links = 'id', 'first_name',


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'id',
