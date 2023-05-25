from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

m = [{'title': 'home', 'url_name': 'home'},
     {'title': 'menu', 'url_name': 'menu'},
     {'title': 'about', 'url_name': 'about'},
     {'title': 'contacts', 'url_name': 'contacts'}]

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order, 'menu1': m[:2], 'menu2': m[2:]})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'menu1': m[:2], 'menu2': m[2:]})
