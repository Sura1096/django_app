import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        "currency": "usd",
                        "product_data": {"name": item.name},
                        "unit_amount": item.price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"session_id": checkout_session.id})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)

    return render(request, "item.html", {"item": item, "stripe_public_key": settings.STRIPE_PUBLIC_KEY})
