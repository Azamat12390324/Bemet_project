from pages.views import PostDetail ,ServiceView, Service
from django.urls import path


app_name = 'pages'

urlpatterns =[
    path('service/', ServiceView.as_view(), name='service'),
    path('<int:pk>/service_detail/', PostDetail.as_view(), name='service_detail'),

    

]
