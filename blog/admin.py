from django.contrib import admin
from blog.models import Blog, Post, Author, PostTag, Comment


#POST_TAG
@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display =('name',)
    list_display_links = ('name',)
    list_filter = ('created_at',)


# POST
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    list_filter = ('created_at',)



#COMMENT
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    list_filter = ('created_at',)



#BLOGFULL
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title', 'author')
    list_filter = ('created_at',)


#AUTHOR
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'image', 'admin_photo']
    list_display_links =['full_name', 'image']
    readonly_fields = ('created_at', 'admin_photo')
