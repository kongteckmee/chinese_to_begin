from django.shortcuts import render


def about(request):
    """
    A view to show the about page
    """
    return render(request, 'about/about.html')
