from django import forms
from .models import Contact
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=False, max_length=50)

    class Meta:
        model = Contact
        fields = ["name", "phone", "email", "address", "message"]

    
