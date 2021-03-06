from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from products.models import Product, Merchandise


# Create your views here.


@login_required()
def view_cart(request):
    """
    View the cart content page
    """
    return render(request, "cart/cart.html")


@login_required()
def add_to_cart(request, id):
    """Add an item to the cart and increase or decrease quantity"""
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    # Get key(id of item) from the value stored in the cart session
    itemInCart = list(cart.keys())[list(cart.values()).index(cart[id])]

    # Check to see if item in cart belongs to merchandise table
    productStored = Merchandise.objects.filter(id=itemInCart).first()
    # Get a list of all merchs in the table
    productsMerch = Merchandise.objects.all()

    request.session["cart"] = cart
    # Redirect the user to the page according to the item stored in cart session
    if productStored in productsMerch:
        return redirect(reverse("products-home"))
    else:
        return redirect(reverse("courses-home"))


@login_required()
def modify_cart(request, id):
    """Enables the user to modify the cart items quantity"""
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity"))

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))

