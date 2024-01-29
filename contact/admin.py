from django.contrib import admin
from contact.models import  ContactModelForm, Contact

@admin.register(ContactModelForm)
class ContactForm(admin.ModelAdmin):
    list_display = ("name", 'email', 'created_at')
    list_display_links = ("name", 'email','created_at')
    search_fields = ("name", 'email', 'message')
    list_filter = ("created_at",)
    
    
@admin.register(Contact)
class Contacts(admin.ModelAdmin):
    list_display = ("phone", 'email', 'created_at')
    list_display_links = ("phone", 'email','created_at')
    search_fields = ( 'email',)
    # list_filter = ("created_at",)
    
