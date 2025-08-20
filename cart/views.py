from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product #Cart, CartItem
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    
    cart = request.session.get('cart', {})  # Example: cart stored in session
    if not cart:
        return redirect('cart')  # if empty cart, go back
    # Create an order
    order = Cart.objects.create(user=request.user)
    # Save order items
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        CartItem.objects.create(order=order, product=product, quantity=quantity)
    # Clear cart
    request.session['cart'] = {}
    return redirect('view_cart', order_id=order.order_id)
    # product = get_object_or_404(Product, id=product_id)
    # cart, created = Cart.objects.get_or_create(user=request.user)
    # # cart, created = Cart.objects.filter(user=request.user)#(user=request.user)
    # # Check if the product is already in cart
    # cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    # if not item_created:
    #     cart_item.quantity += 1
    #     cart_item.save()
    # return redirect('view_cart', cart=cart.order_id)
# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', {})yyuu
#     request.session['cart'] = cart
#     return redirect('home')
# def add_to_cart(request, product_id):
#     user = request.user
#     # product = filter(Product, id=product_id)
#     carts = Cart.objects.filter(user=user, id=product_id)
#     if carts.exists():
#         cart = carts.first()
#     else:
#         cart = Cart.objects.create(user=user, id=product_id)
#         cart.save()
#     return redirect('view_cart')

    # now proceed to add the item to cart...









@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.total_price()
    return render(request, 'cart/view_cart.html', {'cart': cart, 'items': items, 'total': total})
# def view_cart(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total = 0
#     for product_id, quantity in cart.items():
#         product = Product.objects.get(id=product_id)
#         item_total = product.price * quantity
#         total += item_total
#         cart_items.append({
#             'product': product,
#             'quantity': quantity,
#             'item_total': item_total
#         })
#     return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart_item.delete()  # Delete item if quantity set to 0
    return redirect('view_cart')





@login_required
def remove_cart_item(request, product_id):
    cart_item = get_object_or_404(CartItem, id=product_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')

# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     if str(product_id) in cart:
#         del cart[str(product_id)]
#     request.session['cart'] = cart
#     return redirect('view_cart')