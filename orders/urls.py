from django.urls import path
from . import views


urlpatterns = [
    path('orders/checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
    #path('history/', views.order_history, name='order_history'),
]