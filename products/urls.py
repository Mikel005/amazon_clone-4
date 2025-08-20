from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name='home'),  # Home page
    path('', views.product_list, name='home'),  # Home page
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    #path("category/<slug:slug>/preview/", views.category_preview, name="category_preview"),
]