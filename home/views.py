from django.shortcuts import render
from .models import Home
from django.views.generic import ListView


def home(request):
    home = Home.objects.all()
    context ={'home': home}
    paginate_by = 4
    return render(request, 'home.html', context)

