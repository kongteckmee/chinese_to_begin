from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    course = request.session.get('course_detail',{})
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)