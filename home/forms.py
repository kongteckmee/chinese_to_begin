from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form for the user/student to contact the
    store admin
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }