from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from .models import ContactFormSubmission

def render_contact_form(request):
    form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
