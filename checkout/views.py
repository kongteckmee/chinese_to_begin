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
    }

    return render(request, template, context)