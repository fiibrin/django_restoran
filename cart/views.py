from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from Restoran.models import Menu
from .cart import Cart
from .forms import CartAddProductFrom

m = [{'title': 'home', 'url_name': 'home'},
     {'title': 'menu', 'url_name': 'menu'},
     {'title': 'about', 'url_name': 'about'},
     {'title': 'contact', 'url_name': 'contacts'}]

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    form = CartAddProductFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        print(form.errors)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    context = {
        'menu1': m[:2],
        'menu2': m[2:],
        'cart': cart,
    }
    return render(request, 'cart/detail.html', context=context)



