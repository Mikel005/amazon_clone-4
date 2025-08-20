
from django.shortcuts import render, redirect,get_object_or_404
#from orders.models import OrderItem, Order
#from products.models import Product
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem




# Create your views here.
@login_required
def checkout_view(request):
    cart = get_object_or_404(Cart, user=request.user)#get_object_or_404
    if not cart.items.exists():
        return redirect('view_cart')
    total = 0
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        total = sum(item.product.price * item.quantity for item in cart.items.all())
        #new_cart = Cart.objects.create(user=request.user, total=total)
        cart.save()
        #order = Cart.objects.create(user=request.user, total=cart.total_price())  #Order
        for item in cart.items.all():
            CartItem.objects.create(
                cart=cart,
                product=item.product,
                quantity=item.quantity,
                #total=item.product.price  # snapshot of price
            )
        cart.items.all().delete()  # Clear cart after order
        return render(request, 'orders/checkout_success.html', {'cart': cart})
    return render(request, 'orders/checkout_confirm.html', {'cart': cart, 'items': cart.items.all(), 'total': total})
# def checkout(request):
#     cart = request.session.get('cart', {})
#     for product_id, quantity in cart.items():
#         product = Product.objects.get(id=product_id)
#         Order.objects.create(user=request.user, product=product, quantity=quantity)
#     request.session['cart'] = {}
#     return render(request, 'orders/checkout_success.html', {'cart':cart})#{'cart':cart}


@login_required
def order_history(request):  #view_oreders
    orders = Cart.objects.filter(user=request.user).order_by('items')    #Order
    return render(request, 'orders/order_history.html', {'orders':orders})
# def order_history(request):
#     orders = Order.objects.filter(user=request.user).order_by('created_at')
#     return render(request, 'orders/order_history.html', {'orders': orders})