from django.contrib import admin
from about.models import  Post, about,Team, TeamPost, SocialMedia


# POST
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_display_links = ('title', 'body',)
    list_filter = ('created_at',)


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     search_fields = ('admin_photo',)

admin.site.register(Team)
admin.site.register(TeamPost)
admin.site.register(SocialMedia)
    


