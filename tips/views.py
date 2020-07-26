from django.shortcuts import render

# Create your views here.

def tips(request):
    """ A view to show the tips page """
    
    return render(request, 'tips/tips.html')
