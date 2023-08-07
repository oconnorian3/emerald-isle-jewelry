from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactFormSubmission


def render_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/contact_success.html')
