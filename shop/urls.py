from django.urls import path
from shop import views
from.views import ShopView, Post,PostDetail

app_name = 'shop'

urlpatterns =[
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('<int:pk>/shop_detail/', PostDetail.as_view(), name='shop_detail'),
    
]