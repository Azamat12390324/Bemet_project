from django.shortcuts import render
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from blog.models import Blog, Post
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count
from blog.forms import CommentForm
from django.urls import reverse
from django.shortcuts import get_object_or_404




def search_blog(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        blogs = Blog.objects.filter(title__contains=searched)
        return render(request, 'search_blog.html', {'searched' : searched, 'blogs': blogs})
    else:
        return render(request, 'search_blog.html', {})
    

def index(request):
    return render(request, 'home.html')


class BlogView(ListView):

    template_name = 'blog.html'

    def get_queryset(self):
        qs = Post.objects.order_by("-id")
        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tag__name=tag) 
        return qs


class PostDetail(DetailView):
    model = Post
    template_name = 'blog-details.html'


class CommentCreate(CreateView):
    form_class = CommentForm


    def form_valid(self, form):
        print(form.instance)
        form.instance.post = get_object_or_404(Post, pk=self.kwargs('pk'))
        return super().form_valid(form)
    


    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk':self.kwargs.get('pk')}) 
        

    

