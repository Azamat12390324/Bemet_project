from django.db import models
from django.utils.translation import gettext as _
from contact.abstract import BaseModel
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars



class about(models.Model):
    title = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    


class Post(BaseModel):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    body = RichTextField()    
    
    def __str__(self) -> str:
        return f"{self.title[:15]}..."
    

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        
        
class TeamPost(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    bg_image = models.ImageField(upload_to='media/%Y/%m/%d')


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Team Post'
        verbose_name_plural = 'Team Posts'



class SocialMedia(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    sm_url = models.URLField()


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'
        ordering = ['order']



class Team(models.Model):  
    team_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sm = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    info = models.TextField()
    sub_info = models.TextField()
    advice = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    sub_info_image = models.ImageField(upload_to='media/%Y/%m/%d')


    def __str__(self) -> str:
        return self.team_name
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

   
   
    # def admin_photo(self):
    #     return mark_safe('<img src="{}" width="100" />' .format(self.image.url))
    # admin_photo.short_description = 'Image'
    # admin_photo.allow_tags = True

    # def __str__(self) -> str:
    #     return self.full_name     
    
      
       



           
        
        
        