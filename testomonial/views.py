from django.shortcuts import render, redirect
from .forms import TestimonialForm
from django.conf import settings
from .models import Testimonial


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list') 
    else:
        form = TestimonialForm()
    return render(request, 'testomonial/add_testimonial.html', {'form': form})


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testomonial/testimonial_list.html', {'testimonials': testimonials})