from django.shortcuts import render, redirect
from .forms import TestimonialForm


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list') 
    else:
        form = TestimonialForm()
    return render(request, 'add_testimonial.html', {'form': form})
