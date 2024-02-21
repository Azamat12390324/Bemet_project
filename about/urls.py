from django.urls import path
from about.views import AboutView, PostDetail,TeamPostDetail,Post


app_name = 'about'

urlpatterns =[
    path('about', AboutView.as_view(), name='about'),
    path('<int:pk>/services_detail/', PostDetail.as_view(), name='services_detail'),
    # path("", TeamPostView.as_view(), name='team'),
    path('<int:pk>/team/', TeamPostDetail.as_view(), name='team-detail'),
]
