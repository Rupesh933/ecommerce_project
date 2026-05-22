from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}  # Automatically populate the slug field based on the category_name field when creating a new category in the admin interface
    list_display = ('category_name',)

admin.site.register(Category, CategoryAdmin)