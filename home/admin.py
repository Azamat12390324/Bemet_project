from django.contrib import admin
from home.models import Home


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

