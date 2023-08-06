from django import forms
from .models import ContactFormSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'subject', 'message']
