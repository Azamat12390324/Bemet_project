from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse


class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data['contacts'] =  Contact.objects.all()
        return data
    
    def get_success_url(self) -> str:
        return reverse('contact:contact')
    
