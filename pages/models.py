from django.db import models 
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    number = models.CharField(max_length=4)

    
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    





