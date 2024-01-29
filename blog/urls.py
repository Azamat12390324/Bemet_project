from django.urls import path
from blog import views
from.views import BlogView, Post, CommentCreate, PostDetail

app_name = 'blog'

urlpatterns =[
    path("", views.index, name='index'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('search_blog/', views.search_blog, name='search_blog'),
    path('<int:pk>/blog_detail/', PostDetail.as_view(), name='blog_detail'),
    path("<int:pk>/comment/",CommentCreate.as_view(),name='comment'),
]