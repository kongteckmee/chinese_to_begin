from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Collect the user's enquiry using the contact form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }