from django import forms
from contact.models import ContactModelForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModelForm
        exclude = ['created_at',]

