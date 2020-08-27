from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form to collect the user's enquiry
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }