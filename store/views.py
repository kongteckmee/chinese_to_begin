from django.shortcuts import render, get_object_or_404
from .models import Store

from .forms import CourseForm

# Create your views here.

def all_courses(request):
    """ A view to show all courses """

    store = Store.objects.all()

    context = {
        'store': store,
    }
    
    return render(request, 'store/store.html', context)

def course_detail(request, store_id):
    """ A view to show individual course details """

    store = get_object_or_404(Store, pk=store_id)

    context = {
        'store': store,
    }
    
    return render(request, 'store/course_detail.html', context)


def add_course(request):
    """Add a course to the store"""
    form = CourseForm()
    template = 'store/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
