from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n  import i18n_patterns


urlpatterns = [
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('contact', include("contact.urls",namespace='default_1')),
    path('', include('blog.urls',))
]


urlpatterns += i18n_patterns(
    path('', include('contact.urls')),

) 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

