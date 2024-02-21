from django.db import models
from contact.abstract import BaseModel


class Regestrstion(BaseModel):
    name = models.CharField(max_length=50, help_text='your name')
    email = models.EmailField(max_length=255, help_text='your email')
    phone = models.IntegerField(help_text='your phone')
    enquiry = models.CharField(max_length=255, help_text='your enquiry')

    def __str__(self) -> str:
        return self.name
    
    verbose_name = 'Regestration'
    verbose_name_plural = 'Regestrations'
