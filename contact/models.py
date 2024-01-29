from django.db import models
from django.utils.translation import gettext_lazy as _
from contact.abstract import BaseModel


class ContactModelForm(BaseModel):
    name  = models.CharField(max_length=32, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    message = models.TextField(verbose_name=_("message"))
    
    def __str__(self) -> str:
        return f"{self.name}/{self.email}"
    
    class Meta:
        verbose_name = ("Contact form")
        verbose_name_plural = ("Contacts form")
        
        
class Contact(BaseModel):
    maps = models.URLField(verbose_name=_("maps"))
    phone = models.CharField(max_length=35,verbose_name=_("phone"))
    email = models.EmailField(verbose_name=_("email"))
    website = models.URLField(verbose_name=_("website"))  
    address = models.CharField(max_length=100, verbose_name=_("address"))      
    
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
