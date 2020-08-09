from django.shortcuts import render, redirect, reverse, get_object_or_404
from store.models import Store
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

import stripe

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        store_id = request.POST.get("store_id")
        store = get_object_or_404(Store, pk=store_id)

        form_data = {
            'full_name': request.POST.get['full_name'],
            'email': request.POST.get['email'],
            'phone_number': request.POST.get['phone_number'],
            'country': request.POST.get['country'],
            'street_address_1': request.POST.get['street_address_1'],
            'street_address_2': request.POST.get['street_address_2'],
            'town_or_city': request.POST.get['town_or_city'],
            'county': request.POST.get['county'],
            'postcode': request.POST.get['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()

            store = Store.objects.get(id=store_id)
            order_line_item = OrderLineItem(
                order=order,
                store=store,
            )
            order_line_item.save()

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        store_id = request.POST.get("store_id")
        store = get_object_or_404(Store, pk=store_id)
        stripe_total = store.price * 100
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'store': store,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful order
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    # messages.success(request, f'Order successfully processed! \
    #     Your order number is {order_number}. A confirmation \
    #     email will be sent to {order.email}.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)