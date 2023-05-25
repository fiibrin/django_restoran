from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from cart.forms import CartAddProductFrom

m = [{'title': 'home', 'url_name': 'home'},
     {'title': 'menu', 'url_name': 'menu'},
     {'title': 'about', 'url_name': 'about'},
     {'title': 'contacts', 'url_name': 'contacts'}]

def index(request):
    context = {
        'menu1': m[:2],
        'menu2': m[2:],
        'menu_selected': 'home',
        'title': 'Restoran',
    }
    return render(request, 'restoran/index.html', context=context)

def menu(request):
    catalog = Menu.objects.all()
    cats = Category.objects.all()
    cart_product_form = CartAddProductFrom()
    context = {
        'catalog': catalog,
        'cats': cats,
        'menu1': m[:2],
        'menu2': m[2:],
        'menu_selected': 'menu',
        'title': 'Menu',
        'cart_product_form': cart_product_form,
    }
    return render(request, 'restoran/menu.html', context=context)

def about(request):
    context = {
        'menu1': m[:2],
        'menu2': m[2:],
        'menu_selected': 'about',
        'title': 'About',
    }
    return render(request, 'restoran/about.html', context=context)

def contacts(request):
    context = {
        'menu1': m[:2],
        'menu2': m[2:],
        'menu_selected': 'contacts',
        'title': 'Contacts',
    }
    return render(request, 'restoran/contacts.html', context=context)