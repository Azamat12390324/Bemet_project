from django.shortcuts import render
from django.shortcuts import render
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Shop, Post
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count
from blog.forms import CommentForm
from django.urls import reverse
from django.shortcuts import get_object_or_404


class ShopView(ListView):
    template_name = 'shop.html'

    def get_queryset(self):
        qs = Post.objects.order_by("-id")
        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tag__name=tag) 
        return qs


class PostDetail(DetailView):
    model = Post
    template_name = 'shop-details.html'


    def get_success_url(self):
        return reverse('shop:detail', kwargs={'pk':self.kwargs.get('pk')}) 
        

    

