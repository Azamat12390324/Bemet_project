from django.shortcuts import render
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from pages.models import Service

class ServiceView(ListView):
    template_name = 'services.html'


    def get_queryset(self) -> QuerySet[Any]:
        qs = Service.objects.all()

        return qs 



class PostDetail(DetailView):
    model = Service
    template_name = 'services-details.html'
    
    def get_success_url(self):
        return reverse('service:detail', kwargs={'pk':self.kwargs.get('pk')}) 
        


  


