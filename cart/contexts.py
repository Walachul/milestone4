from django.shortcuts import get_object_or_404
from products.models import Merchandise
from courses.models import Courses


def cart_contents(request):
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
        merchandise = get_object_or_404(Merchandise, pk=id)
        course = get_object_or_404(Courses, pk=id)
        total += quantity * merchandise.price
        item_count += quantity
        cart_items.append(
            {
                "id": id,
                "quantity": quantity,
                "merchandise": merchandise,
                "course": course,
            }
        )

    return {"cart_items": cart_items, "total": total, "item_count": item_count}

