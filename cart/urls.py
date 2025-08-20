from django.urls import path
from . import views


urlpatterns = [
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/update/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
]