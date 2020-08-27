from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    """Initialize the contact form"""
    form = ContactForm()

    if 'contact-form' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {"form": form, }

    return render(request, "home/index.html", context)
