from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    context = {"form": form, }

    return render(request, "home/index.html", context)
