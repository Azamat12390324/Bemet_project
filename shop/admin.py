from django.contrib import admin
from shop.models import Shop, Post




# POST
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    list_filter = ('created_at',)


#BLOGFULL
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title', 'author')
    list_filter = ('created_at',)



