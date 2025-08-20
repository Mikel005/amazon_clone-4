from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', default=1)
    
    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')
    name=models.CharField(max_length=200)
    image = models.ImageField(upload_to='subcategories', blank=True, null=True, default=1)
    
    def __str__(self):
        return f"{self.category.name}-{self.name}"
    
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='media/')
    # def __str__(self):
    #     return self.title