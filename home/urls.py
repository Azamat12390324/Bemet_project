from django.urls import path
from home import views

app_name = 'home'


urlpatterns = [
    path('home_1', views.home, name='home'),
        
]

    
