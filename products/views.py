from django.shortcuts import render, get_object_or_404
from .models import Product, Category, SubCategory
import random

# Create your views here.
# def home(request)
#     return render(request, 'base.html')



def home(request):
    categories = Category.objects.prefetch_related('subcategories__products').all()[:4]
    # # Example: pick 4 products from specific categories
    # cloths_products = Product.objects.filter(subcategory__category__name="cloths").order_by("?")[:4]
    # Electronics_products = Product.objects.filter(subcategory__category__name="Electronics").order_by("?")[:4]
    # # # Example: pick 4 from a specific subcategory
    # phones_products = Product.objects.filter(subcategory__category__name="phones").order_by("?")[:4]
    # print("Eletronics:", Electronics_products)
    # print("phones:", phones_products)
    # print("cloths:", cloths_products)
    # context = {
    #         "categories": categories,
    #         "cloths_products":cloths_products,
    #         "Electronics_products":Electronics_products,
    #         "phones_products":phones_products,
            
    #     }
    return render(request, 'base.html', {"categories": categories})
# def category_preview(request, slug):
#     category = Category.objects.prefetch_related("subcategories__products").get(slug=slug)
#     all_products = Product.objects.filter(subcategories__catgory=category)
#     products = all_products.order_by('?')[:4]
#     return render(request, "category_preview.html", {"category":category, "products":products})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products': products})#products/product_list.html
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    categories = categories.prefetch_related('products')
    return render(request, 'products/product_detail.html', {'product': product})
def category_list(request):
    categories = Category.object.prefectch_related('subcategories')
    return render(request, 'products/product_list.html', {'categories':categories}),

