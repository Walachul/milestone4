from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """
    View the cart content page
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, id):
    """
    Add an item to the cart and increase or decrease quantity
    """
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    cart[id] = cart.get(id, quantity)

    request.session["cart"] = cart

    return redirect(reverse("products-home"))


def modify_cart(request, id):
    """
    Enables the user to modify the cart items quantity
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))

