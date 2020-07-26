from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view to show the about page """
    
    return render(request, 'about/about.html')