from django.db import models
from django.utils.translation import gettext as _
from contact.abstract import BaseModel
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars


class   Blog(BaseModel):
    title = models.CharField(max_length=255, help_text=_('Write title'), verbose_name=_('title'))
    author = models.CharField(max_length=30, help_text=_('Write author'), verbose_name=_('author'))
    photo = models.ImageField(upload_to='blog/photos/',verbose_name=_('photo'), default='default')


    def __str__(self) -> str:
        return self.title[:10]
    

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class Author(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_('full_name'))
    image = models.ImageField(upload_to='author_images/', verbose_name=_('image'))

    @property
    def  short_description(self):
        return truncatechars(self.full_name)
    

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />' .format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.full_name
    
    

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
    


class PostTag(BaseModel):
    name = models.CharField(max_length=30, verbose_name=_('name'))


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name =_('Tag')
        verbose_name = _('Tags')


class Post(BaseModel):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    body = RichTextField()
    article = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_image/', verbose_name=_('image'))
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name="posts")
    tag = models.ManyToManyField(PostTag, verbose_name=_('tag'), related_name="posts")

    
    def __str__(self) -> str:
        return f"{self.title[:15]}..."
    


    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Comment(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'))


    def __str__(self) -> str:
        return f"{self.name}\n{self.email}\n{self.comment}"
    

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = ('Comments')

