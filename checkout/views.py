from django.shortcuts import render, get_object_or_404
from store.models import Store
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    store_id = request.POST.get("store_id")
    store = get_object_or_404(Store, pk=store_id)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'store': store,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HE74LC0nQTzHANK8xu8Ua95gHrrPJ02v5R5YcXBtT3ELHVjEyjjSirrIXnsd26VJ2Z0gkt9RGUbcNthUyBFRGze00m5HXSrxt',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)