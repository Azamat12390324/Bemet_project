from django.urls import path
from regestration.views import regestration


app_name = 'regestration'


urlpatterns = [
    path('regestration/', regestration, name='regestration'),
]
