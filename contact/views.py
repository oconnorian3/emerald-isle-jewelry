from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactFormSubmission

def render_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            
            return redirect('home')  # Replace 'success-page' with the URL of a success page
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
