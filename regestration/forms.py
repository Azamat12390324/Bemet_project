from django import forms
from regestration.models import Regestrstion

class Regestrstion(forms.ModelForm):
    class Meta:
        model = Regestrstion
        fields = ('name', 'email', 'phone', 'enquiry',)
