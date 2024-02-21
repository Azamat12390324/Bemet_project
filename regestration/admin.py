from django.contrib import admin
from regestration.models import  Regestrstion

@admin.register(Regestrstion)
class Regestrstion(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone', 'enquiry',)
    list_display_links = ("name", 'email',)
    search_fields = ("name", 'email',)
    list_filter = ("created_at",)
