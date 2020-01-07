from django.shortcuts import get_object_or_404
from products.models import Merchandise, Clothes


def cart_content(request):
    """
    Stores the cart items and keeps them in the session when the user is logged in
    and he navigates the site.
    Cart items are gone when the user logs out.
    """
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0
    item_count = 0

    for id, quantity in cart.items():
        merch = get_object_or_404(Merchandise, pk=id)
        total += quantity * merch.price
        item_count += quantity
        cart_items.append({"id": id, "quantity": quantity, "merch": merch})

    return {"cart_items": cart_items, "total": total, "item_count": item_count}

