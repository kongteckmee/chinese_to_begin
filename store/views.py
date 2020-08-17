from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Store, Category

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
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        return redirect(reverse('store'))
        # else:
        #     return f'{"Failed to add course. Please ensure the form is valid."}'
    else:
        form = CourseForm()

    template = 'store/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_course(request, store_id):
    """Edit a course in the store"""
    # store_id = request.POST.get("store_id")
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Successfully updated product!')
            return redirect(reverse('store'))
        # else:
            # return f'{"Failed to add course. Please ensure the form is valid."}'
    else:
        form = CourseForm(instance=store)
        # return f'{store.name}'
        # messages.info(request, f'You are editing {store.name}')

    template = 'store/edit_course.html'
    context = {
        'form': form,
        'store': store,
    }
    return render(request, template, context)


def delete_course(request, store_id):
    """Delete a course from the store"""
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return redirect(reverse('store'))
