from django.shortcuts import render
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import about
from about.models import about, Post, Team, TeamPost


class AboutView(ListView):
    template_name = 'about.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = Team.objects.all()

        return qs 
        
    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['post_icon'] = Post.objects.all()

        return data


class PostDetail(DetailView):
    model = Post
    template_name = 'services-details.html'
    

    
    def get_success_url(self):
        return reverse('services:detail', kwargs={'pk':self.kwargs.get('pk')}) 
        

# class TeamPostView(ListView):
#     model = Team
#     # template_name = 'about.html'


    # def get_queryset(self) -> QuerySet[Any]:
    #     qs = Team.objects.all()

    #     return qs 
    


class TeamPostDetail(DetailView):
    model = Team
    template_name = 'team-details.html'

    def get_success_url(self):
        return reverse('team:detail', kwargs={'pk':self.kwargs.get('pk')}) 
       