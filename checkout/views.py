from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderForm, StripePayForm
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        stripe_form = StripePayForm(request.POST)

        if order_form.is_valid() and stripe_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.buyer = request.user
            order.save()
            """Get information from cart session """
            cart = request.session.get("cart", {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_item = OrderItem(order=order, product=product, quantity=quantity)
                order_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="RON",
                    description=request.user.email,
                    card=stripe_form.cleaned_data["stripe_id"],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "Payment was successful!")
                request.session["cart"] = {}
                return redirect(reverse("products-home"))
            else:
                messages.error(request, "Payment was not completed")
        else:
            print(stripe_form)
            messages.error(request, "Unable to take payment with that card!")
    else:
        order_form = OrderForm()
        stripe_form = StripePayForm()
    return render(
        request,
        "checkout/checkout.html",
        {
            "order_form": order_form,
            "stripe_form": stripe_form,
            "publishable": settings.STRIPE_PUBLISHABLE,
        },
    )

