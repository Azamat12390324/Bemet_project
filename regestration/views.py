from django.shortcuts import render, redirect
from regestration.forms import Regestrstion

def regestration(request):
    if request.method == 'POST':
        form = Regestrstion(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Regestrstion()

    return render(request, 'regestration/register.html', {'form': form})
