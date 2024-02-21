from django.db import models


class Home(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='home/image', blank=True)
    slide = models.ImageField(upload_to='home/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='home/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    icons = models.ImageField(upload_to='home/icons/', blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'
