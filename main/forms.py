from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=400)