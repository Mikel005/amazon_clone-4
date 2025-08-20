from django.contrib import admin
from .models import Product, Category, SubCategory


# Register your models here.
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    
    
admin.site.register(Product)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory)