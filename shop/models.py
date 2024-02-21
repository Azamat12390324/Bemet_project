from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from contact.abstract import BaseModel
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars


class Shop(BaseModel):
    title = models.CharField(max_length=255, help_text=_('Write title'), verbose_name=_('title'))
    author = models.CharField(max_length=30, help_text=_('Write author'), verbose_name=_('author'))
    photo = models.ImageField(upload_to='shop/photos/',verbose_name=_('photo'), default='default')

class Post(BaseModel):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    sub_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_image/', verbose_name=_('image'))
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    
    def __str__(self) -> str:
        return f"{self.title[:15]}..."
    


    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')