from django.shortcuts import render


def tips(request):
    """
    A view to show the tips page
    """
    return render(request, 'tips/tips.html')
