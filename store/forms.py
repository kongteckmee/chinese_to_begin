from django import forms
from .models import Store, Category


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Store
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)