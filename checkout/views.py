from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def checkout(request, store_id):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)