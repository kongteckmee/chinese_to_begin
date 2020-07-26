from django.shortcuts import render
from .models import Store

# Create your views here.

def all_courses(request):
    """ A view to show all courses """

    store = Store.objects.all()

    context = {
        'store': store,
    }
    
    return render(request, 'store/store.html', context)
