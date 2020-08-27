from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def contact(request):
    """Initialize the contact form"""
    contact_form = ContactForm()

    if 'contact-form' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()

            return redirect('index')

    context = {"contact_form": contact_form, }

    return render(request, "home/index.html", context)
