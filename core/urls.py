from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n  import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls", namespace='default_1')),
    path('blog/', include('blog.urls', namespace='default_2')),
    path('about/',include('about.urls',namespace='default_4')),
    path('shop/', include('shop.urls',namespace='default_5')),
    path('home/', include('home.urls', namespace='default_3')),
    path('pages/',include('pages.urls',namespace='default_6')),
    path('regestration/', include('regestration.urls'))
    
]


urlpatterns += i18n_patterns(
    path('', include('contact.urls')),
    path('',include('blog.urls')),
    path('',include('home.urls')),
    path('',include('about.urls')),
    path('',include('shop.urls')),
    path('',include('pages.urls')),
    

) 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

